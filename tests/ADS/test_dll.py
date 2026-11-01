
import pytest
from ADS.linked_lists import DLL, DLLNode


"""
Tests for the DLL implementation in ADS/linked_lists.py.

Run from the repository root:
    python -m pytest tests/ADS/test_dll.py -v

Assumed public API:
    DLL(*values)
    dll.append(value)
    dll.pop()                 # removes and returns the tail node
    dll.insert(value, index=0)
    dll.remove(index=0)       # removes and returns the node at index
    dll.extend(other_dll)     # appends the other list's values; does not mutate it
    dll[index]                # supports positive and Python-style negative indices

The tests deliberately check node identity and both directions of every link,
not just the values produced by iteration.
"""


def values(dll):
    """Return the values in a DLL without relying on its __str__ method."""
    return [node.val for node in dll]


def assert_dll_invariants(dll, expected_values):
    """Check size, endpoints, forward links, backward links, and iteration."""
    expected_values = list(expected_values)
    expected_size = len(expected_values)

    assert len(dll) == expected_size
    assert dll.size == expected_size
    assert values(dll) == expected_values

    if expected_size == 0:
        assert dll.head is None
        assert dll.tail is None
        return

    assert dll.head is not None
    assert dll.tail is not None
    assert dll.head.prev is None
    assert dll.tail.next is None

    # Walk forward and verify every prev/next relationship.
    current = dll.head
    previous = None
    forward_nodes = []

    while current is not None:
        assert current.prev is previous
        forward_nodes.append(current)
        previous = current
        current = current.next

    assert len(forward_nodes) == expected_size
    assert forward_nodes[0] is dll.head
    assert forward_nodes[-1] is dll.tail

    # Walk backward and verify that we visit the exact same nodes in reverse.
    current = dll.tail
    following = None
    backward_nodes = []

    while current is not None:
        assert current.next is following
        backward_nodes.append(current)
        following = current
        current = current.prev

    assert len(backward_nodes) == expected_size
    assert backward_nodes == forward_nodes[::-1]


@pytest.fixture
def empty_dll():
    return DLL()


@pytest.fixture
def populated_dll():
    return DLL(10, 20, 30, 40)


# ---------------------------------------------------------------------------
# Construction and basic interface
# ---------------------------------------------------------------------------

def test_empty_constructor(empty_dll):
    assert_dll_invariants(empty_dll, [])


def test_constructor_with_multiple_values(populated_dll):
    assert_dll_invariants(populated_dll, [10, 20, 30, 40])


def test_constructor_with_one_value():
    dll = DLL(42)
    assert_dll_invariants(dll, [42])


def test_constructor_preserves_values_as_single_items():
    # A list passed as one argument should remain one value, not be unpacked.
    payload = [1, 2, 3]
    dll = DLL(payload)

    assert len(dll) == 1
    assert dll.head.val is payload
    assert dll.tail is dll.head


def test_public_endpoint_and_size_properties(populated_dll):
    assert populated_dll.head is not None
    assert populated_dll.tail is not None
    assert populated_dll.size == 4


def test_read_only_public_properties(populated_dll):
    # Public properties should not be assignable.
    with pytest.raises(AttributeError):
        populated_dll.head = None

    with pytest.raises(AttributeError):
        populated_dll.tail = None

    with pytest.raises(AttributeError):
        populated_dll.size = 100


# ---------------------------------------------------------------------------
# Iteration and string representations
# ---------------------------------------------------------------------------

def test_iteration_yields_nodes(populated_dll):
    nodes = list(populated_dll)

    assert len(nodes) == 4
    assert [node.val for node in nodes] == [10, 20, 30, 40]
    assert nodes[0] is populated_dll.head
    assert nodes[-1] is populated_dll.tail


def test_iteration_over_empty_list(empty_dll):
    assert list(empty_dll) == []


def test_str_representation(populated_dll):
    assert str(populated_dll) == "LinkedList([10, 20, 30, 40])"


def test_str_representation_of_empty_list(empty_dll):
    assert str(empty_dll) == "LinkedList([])"


def test_repr_contains_each_node_once(populated_dll):
    representation = repr(populated_dll)

    # Avoid assuming a particular DLLNode.__str__ formatting.
    for value in (10, 20, 30, 40):
        assert str(value) in representation

    assert representation.count("<=>") == 3


# ---------------------------------------------------------------------------
# Indexing
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    ("index", "expected"),
    [
        (0, 10),
        (1, 20),
        (2, 30),
        (3, 40),
        (-1, 40),
        (-2, 30),
        (-3, 20),
        (-4, 10),
    ],
)
def test_getitem_valid_indices(populated_dll, index, expected):
    assert populated_dll[index].val == expected


@pytest.mark.parametrize("index", [4, 5, -5, -100])
def test_getitem_out_of_range(populated_dll, index):
    with pytest.raises(IndexError):
        _ = populated_dll[index]


@pytest.mark.parametrize("index", [1.5, "1", None, (1,)])
def test_getitem_rejects_non_integer_indices(populated_dll, index):
    with pytest.raises(TypeError):
        _ = populated_dll[index]


def test_getitem_on_empty_list(empty_dll):
    with pytest.raises(IndexError):
        _ = empty_dll[0]

    with pytest.raises(IndexError):
        _ = empty_dll[-1]


# ---------------------------------------------------------------------------
# append
# ---------------------------------------------------------------------------

def test_append_to_empty_list(empty_dll):
    result = empty_dll.append(10)

    assert result is None
    assert_dll_invariants(empty_dll, [10])


def test_append_to_nonempty_list(populated_dll):
    old_tail = populated_dll.tail

    populated_dll.append(50)

    assert populated_dll.tail is not old_tail
    assert populated_dll.tail.prev is old_tail
    assert old_tail.next is populated_dll.tail
    assert_dll_invariants(populated_dll, [10, 20, 30, 40, 50])


def test_append_multiple_values():
    dll = DLL()

    for value in range(10):
        dll.append(value)

    assert_dll_invariants(dll, list(range(10)))


# ---------------------------------------------------------------------------
# pop
# ---------------------------------------------------------------------------

def test_pop_from_empty_list(empty_dll):
    with pytest.raises(IndexError):
        empty_dll.pop()

    assert_dll_invariants(empty_dll, [])


def test_pop_single_element():
    dll = DLL(10)
    removed = dll.pop()

    assert isinstance(removed, DLLNode)
    assert removed.val == 10
    assert removed.prev is None
    assert removed.next is None
    assert_dll_invariants(dll, [])


def test_pop_from_multiple_elements(populated_dll):
    old_tail = populated_dll.tail
    new_tail = old_tail.prev

    removed = populated_dll.pop()

    assert removed is old_tail
    assert removed.val == 40
    assert removed.prev is None
    assert removed.next is None
    assert new_tail is populated_dll.tail
    assert new_tail.next is None
    assert_dll_invariants(populated_dll, [10, 20, 30])


def test_pop_until_empty(populated_dll):
    removed_values = []

    while len(populated_dll):
        removed_values.append(populated_dll.pop().val)
        assert_dll_invariants(populated_dll, [10, 20, 30, 40][:len(populated_dll)])

    assert removed_values == [40, 30, 20, 10]
    assert_dll_invariants(populated_dll, [])


# ---------------------------------------------------------------------------
# insert
# API assumed: insert(value, index=0)
# Valid insertion positions are 0 through len(dll), inclusive.
# ---------------------------------------------------------------------------

def test_insert_into_empty_list():
    dll = DLL()
    dll.insert(10, index=0)

    assert_dll_invariants(dll, [10])


def test_insert_at_head(populated_dll):
    populated_dll.insert(5, index=0)

    assert_dll_invariants(populated_dll, [5, 10, 20, 30, 40])


def test_insert_in_middle(populated_dll):
    populated_dll.insert(25, index=2)

    assert_dll_invariants(populated_dll, [10, 20, 25, 30, 40])


def test_insert_at_end(populated_dll):
    populated_dll.insert(50, index=4)

    assert_dll_invariants(populated_dll, [10, 20, 30, 40, 50])


def test_insert_at_end_of_empty_list():
    dll = DLL()
    dll.insert(10, index=0)

    assert_dll_invariants(dll, [10])


@pytest.mark.parametrize("index", [-1, -5, 5, 100])
def test_insert_rejects_invalid_indices(populated_dll, index):
    with pytest.raises(IndexError):
        populated_dll.insert(99, index=index)

    assert_dll_invariants(populated_dll, [10, 20, 30, 40])


@pytest.mark.parametrize("index", [1.5, "1", None])
def test_insert_rejects_non_integer_indices(populated_dll, index):
    with pytest.raises(TypeError):
        populated_dll.insert(99, index=index)

    assert_dll_invariants(populated_dll, [10, 20, 30, 40])


# ---------------------------------------------------------------------------
# remove
# API assumed: remove(index=0), returning the detached removed node.
# ---------------------------------------------------------------------------

def test_remove_from_empty_list(empty_dll):
    with pytest.raises((IndexError, ValueError)):
        empty_dll.remove()

    assert_dll_invariants(empty_dll, [])


def test_remove_only_element():
    dll = DLL(10)
    removed = dll.remove(0)

    assert isinstance(removed, DLLNode)
    assert removed.val == 10
    assert removed.prev is None
    assert removed.next is None
    assert_dll_invariants(dll, [])


def test_remove_head(populated_dll):
    old_head = populated_dll.head

    removed = populated_dll.remove(0)

    assert removed is old_head
    assert removed.val == 10
    assert removed.prev is None
    assert removed.next is None
    assert populated_dll.head.prev is None
    assert_dll_invariants(populated_dll, [20, 30, 40])


def test_remove_middle(populated_dll):
    removed = populated_dll.remove(1)

    assert removed.val == 20
    assert removed.prev is None
    assert removed.next is None
    assert_dll_invariants(populated_dll, [10, 30, 40])


def test_remove_tail(populated_dll):
    old_tail = populated_dll.tail

    removed = populated_dll.remove(3)

    assert removed is old_tail
    assert removed.val == 40
    assert removed.prev is None
    assert removed.next is None
    assert populated_dll.tail.next is None
    assert_dll_invariants(populated_dll, [10, 20, 30])


@pytest.mark.parametrize("index", [-1, 4, 100])
def test_remove_rejects_invalid_indices(populated_dll, index):
    with pytest.raises(IndexError):
        populated_dll.remove(index)

    assert_dll_invariants(populated_dll, [10, 20, 30, 40])


@pytest.mark.parametrize("index", [1.5, "1", None])
def test_remove_rejects_non_integer_indices(populated_dll, index):
    with pytest.raises(TypeError):
        populated_dll.remove(index)

    assert_dll_invariants(populated_dll, [10, 20, 30, 40])


# ---------------------------------------------------------------------------
# extend
# Assumed contract: append copies of the source values, leaving source intact.
# ---------------------------------------------------------------------------

def test_extend_nonempty_list():
    target = DLL(1, 2)
    source = DLL(3, 4)

    target.extend(source)

    assert_dll_invariants(target, [1, 2, 3, 4])
    assert_dll_invariants(source, [3, 4])

    # The two lists should not share nodes.
    target_nodes = {id(node) for node in target}
    source_nodes = {id(node) for node in source}
    assert target_nodes.isdisjoint(source_nodes)


def test_extend_empty_target():
    target = DLL()
    source = DLL(1, 2, 3)

    target.extend(source)

    assert_dll_invariants(target, [1, 2, 3])
    assert_dll_invariants(source, [1, 2, 3])


def test_extend_empty_source():
    target = DLL(1, 2)
    source = DLL()

    target.extend(source)

    assert_dll_invariants(target, [1, 2])
    assert_dll_invariants(source, [])


def test_extend_with_empty_target_and_empty_source():
    target = DLL()
    source = DLL()

    target.extend(source)

    assert_dll_invariants(target, [])
    assert_dll_invariants(source, [])


def test_extend_does_not_share_mutable_values():
    # This checks node ownership, not deep-copying of the values themselves.
    payload = {"items": [1]}
    source = DLL(payload)
    target = DLL()

    target.extend(source)

    assert target.head is not source.head
    assert target.head.val is payload
    assert source.head.val is payload


def test_extend_self_is_rejected_without_corrupting_list():
    dll = DLL(1, 2, 3)

    with pytest.raises((ValueError, TypeError)):
        dll.extend(dll)

    assert_dll_invariants(dll, [1, 2, 3])


# ---------------------------------------------------------------------------
# Mixed operations: useful for catching bugs that isolated tests miss.
# ---------------------------------------------------------------------------

def test_mixed_operations_preserve_all_invariants():
    dll = DLL()

    dll.append(10)
    assert_dll_invariants(dll, [10])

    dll.append(30)
    assert_dll_invariants(dll, [10, 30])

    dll.insert(20, index=1)
    assert_dll_invariants(dll, [10, 20, 30])

    removed = dll.remove(1)
    assert removed.val == 20
    assert_dll_invariants(dll, [10, 30])

    dll.insert(5, index=0)
    assert_dll_invariants(dll, [5, 10, 30])

    popped = dll.pop()
    assert popped.val == 30
    assert_dll_invariants(dll, [5, 10])

    dll.remove(0)
    assert_dll_invariants(dll, [10])

    dll.pop()
    assert_dll_invariants(dll, [])
