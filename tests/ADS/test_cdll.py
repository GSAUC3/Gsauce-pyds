
import pytest
from copy import deepcopy

from ADS.linked_lists import CircularDLL


# ============================================================
# FIXTURES
# ============================================================

@pytest.fixture
def empty_cdll():
    return CircularDLL()


@pytest.fixture
def populated_cdll():
    return CircularDLL(10, 20, 30, 40)


# ============================================================
# INVARIANT CHECKER
# ============================================================

def assert_cdll_invariants(ll, expected):
    """
    Verify structural and circular invariants of CircularDLL.
    """

    assert len(ll) == len(expected)
    assert ll.size == len(expected)

    # Empty-list invariants
    if not expected:
        assert ll.head is None
        assert ll.tail is None
        return

    assert ll.head is not None
    assert ll.tail is not None

    # Circular connections
    assert ll.tail.next is ll.head
    assert ll.head.prev is ll.tail

    current = ll.head
    visited = []

    for _ in range(len(expected)):
        assert current is not None

        visited.append(current.val)

        # Bidirectional pointer invariants
        assert current.next.prev is current
        assert current.prev.next is current

        current = current.next

    # Exactly size nodes should bring us back to head
    assert current is ll.head

    assert visited == expected

    # Verify unique nodes
    nodes = []
    current = ll.head

    for _ in range(len(expected)):
        assert all(current is not node for node in nodes)
        nodes.append(current)
        current = current.next

    assert nodes[-1] is ll.tail


# ============================================================
# CONSTRUCTOR TESTS
# ============================================================

def test_constructor_empty():
    ll = CircularDLL()

    assert_cdll_invariants(ll, [])


def test_constructor_single_element():
    ll = CircularDLL(10)

    assert_cdll_invariants(ll, [10])


def test_constructor_multiple_elements():
    ll = CircularDLL(10, 20, 30)

    assert_cdll_invariants(ll, [10, 20, 30])


def test_constructor_preserves_order():
    ll = CircularDLL(5, 10, 15, 20)

    assert_cdll_invariants(ll, [5, 10, 15, 20])


def test_constructor_with_none():
    ll = CircularDLL(None)

    assert_cdll_invariants(ll, [None])


# ============================================================
# APPEND TESTS
# ============================================================

def test_append_empty_list(empty_cdll):
    empty_cdll.append(10)

    assert_cdll_invariants(empty_cdll, [10])


def test_append_multiple_elements(empty_cdll):
    empty_cdll.append(10)
    empty_cdll.append(20)
    empty_cdll.append(30)

    assert_cdll_invariants(empty_cdll, [10, 20, 30])


def test_append_to_populated_list(populated_cdll):
    populated_cdll.append(50)

    assert_cdll_invariants(
        populated_cdll,
        [10, 20, 30, 40, 50]
    )


def test_append_updates_head_and_tail(empty_cdll):
    empty_cdll.append(10)

    assert empty_cdll.head is empty_cdll.tail
    assert empty_cdll.head.next is empty_cdll.head
    assert empty_cdll.head.prev is empty_cdll.head


def test_append_preserves_head(populated_cdll):
    old_head = populated_cdll.head

    populated_cdll.append(50)

    assert populated_cdll.head is old_head


def test_append_updates_tail(populated_cdll):
    old_tail = populated_cdll.tail

    populated_cdll.append(50)

    assert populated_cdll.tail is not old_tail
    assert populated_cdll.tail.val == 50


def test_append_preserves_existing_nodes(populated_cdll):
    old_nodes = [
        populated_cdll[i]
        for i in range(len(populated_cdll))
    ]

    populated_cdll.append(50)

    for i, node in enumerate(old_nodes):
        assert populated_cdll[i] is node


def test_append_maintains_circularity(populated_cdll):
    populated_cdll.append(50)

    assert populated_cdll.tail.next is populated_cdll.head
    assert populated_cdll.head.prev is populated_cdll.tail


# ============================================================
# INSERT TESTS
# ============================================================

def test_insert_into_empty_list(empty_cdll):
    empty_cdll.insert(10, 0)

    assert_cdll_invariants(empty_cdll, [10])


def test_insert_at_head(populated_cdll):
    populated_cdll.insert(5, 0)

    assert_cdll_invariants(
        populated_cdll,
        [5, 10, 20, 30, 40]
    )


def test_insert_at_middle(populated_cdll):
    populated_cdll.insert(25, 2)

    assert_cdll_invariants(
        populated_cdll,
        [10, 20, 25, 30, 40]
    )


def test_insert_at_tail(populated_cdll):
    populated_cdll.insert(50, 4)

    assert_cdll_invariants(
        populated_cdll,
        [10, 20, 30, 40, 50]
    )


def test_insert_at_head_updates_head(populated_cdll):
    old_head = populated_cdll.head

    populated_cdll.insert(5, 0)

    assert populated_cdll.head.val == 5
    assert populated_cdll.head.next is old_head
    assert old_head.prev is populated_cdll.head


def test_insert_at_tail_updates_tail(populated_cdll):
    old_tail = populated_cdll.tail

    populated_cdll.insert(50, 4)

    assert populated_cdll.tail.val == 50
    assert populated_cdll.tail.prev is old_tail


def test_insert_single_element_into_empty_list(empty_cdll):
    empty_cdll.insert(10, 0)

    assert empty_cdll.head is empty_cdll.tail
    assert empty_cdll.head.next is empty_cdll.head
    assert empty_cdll.head.prev is empty_cdll.head


def test_insert_preserves_existing_nodes(populated_cdll):
    old_nodes = [
        populated_cdll[i]
        for i in range(4)
    ]

    populated_cdll.insert(25, 2)

    assert populated_cdll[0] is old_nodes[0]
    assert populated_cdll[1] is old_nodes[1]
    assert populated_cdll[3] is old_nodes[2]
    assert populated_cdll[4] is old_nodes[3]


@pytest.mark.parametrize("index", [5, 10])
def test_insert_invalid_index(populated_cdll, index):
    with pytest.raises(IndexError):
        populated_cdll.insert(50, index)


@pytest.mark.parametrize("index", ["1", 1.5, None])
def test_insert_invalid_index_type(populated_cdll, index):
    with pytest.raises(TypeError):
        populated_cdll.insert(50, index)


# # ============================================================
# # POP TESTS
# # ============================================================

def test_pop_empty_list(empty_cdll):
    with pytest.raises(IndexError):
        empty_cdll.pop()


def test_pop_single_element():
    ll = CircularDLL(10)

    removed = ll.pop()

    assert removed.val == 10
    assert removed.next is None
    assert removed.prev is None

    assert_cdll_invariants(ll, [])


def test_pop_multiple_elements(populated_cdll):
    removed = populated_cdll.pop()

    assert removed.val == 40
    assert removed.next is None
    assert removed.prev is None

    assert_cdll_invariants(
        populated_cdll,
        [10, 20, 30]
    )


def test_pop_updates_tail(populated_cdll):
    old_tail = populated_cdll.tail

    populated_cdll.pop()

    assert populated_cdll.tail is not old_tail
    assert populated_cdll.tail.val == 30


def test_pop_preserves_head(populated_cdll):
    old_head = populated_cdll.head

    populated_cdll.pop()

    assert populated_cdll.head is old_head


def test_pop_updates_circular_connections(populated_cdll):
    populated_cdll.pop()

    assert populated_cdll.tail.next is populated_cdll.head
    assert populated_cdll.head.prev is populated_cdll.tail


def test_pop_until_empty(populated_cdll):
    for _ in range(4):
        populated_cdll.pop()

    assert_cdll_invariants(populated_cdll, [])


def test_pop_returns_original_tail(populated_cdll):
    old_tail = populated_cdll.tail

    removed = populated_cdll.pop()

    assert removed is old_tail


# # ============================================================
# # REMOVE TESTS
# # ============================================================

def test_remove_head(populated_cdll):
    old_head = populated_cdll.head

    removed = populated_cdll.remove(0)

    assert removed is old_head
    assert removed.val == 10
    assert removed.next is None
    assert removed.prev is None

    assert_cdll_invariants(
        populated_cdll,
        [20, 30, 40]
    )


def test_remove_middle(populated_cdll):
    removed = populated_cdll.remove(1)

    assert removed.val == 20
    assert removed.next is None
    assert removed.prev is None

    assert_cdll_invariants(
        populated_cdll,
        [10, 30, 40]
    )


def test_remove_tail(populated_cdll):
    old_tail = populated_cdll.tail

    removed = populated_cdll.remove(3)

    assert removed is old_tail
    assert removed.val == 40
    assert removed.next is None
    assert removed.prev is None

    assert_cdll_invariants(
        populated_cdll,
        [10, 20, 30]
    )


def test_remove_only_element():
    ll = CircularDLL(10)

    removed = ll.remove(0)

    assert removed.val == 10
    assert removed.next is None
    assert removed.prev is None

    assert_cdll_invariants(ll, [])


def test_remove_from_empty_list(empty_cdll):
    with pytest.raises(IndexError):
        empty_cdll.remove(0)


@pytest.mark.parametrize("index", [4, 10])
def test_remove_invalid_index(populated_cdll, index):
    with pytest.raises(IndexError):
        populated_cdll.remove(index)


@pytest.mark.parametrize("index", ["1", 1.5, None])
def test_remove_invalid_index_type(populated_cdll, index):
    with pytest.raises(TypeError):
        populated_cdll.remove(index)


def test_remove_updates_circular_connections(populated_cdll):
    populated_cdll.remove(1)

    assert_cdll_invariants(
        populated_cdll,
        [10, 30, 40]
    )


def test_remove_all_elements(populated_cdll):
    for _ in range(4):
        populated_cdll.remove(0)

    assert_cdll_invariants(populated_cdll, [])


def test_remove_preserves_remaining_nodes(populated_cdll):
    old_nodes = [
        populated_cdll[i]
        for i in range(4)
    ]

    populated_cdll.remove(1)

    assert populated_cdll[0] is old_nodes[0]
    assert populated_cdll[1] is old_nodes[2]
    assert populated_cdll[2] is old_nodes[3]


# # ============================================================
# # GETITEM TESTS
# # ============================================================

def test_getitem_first(populated_cdll):
    assert populated_cdll[0].val == 10


def test_getitem_middle(populated_cdll):
    assert populated_cdll[2].val == 30


def test_getitem_last(populated_cdll):
    assert populated_cdll[3].val == 40


def test_getitem_returns_original_node(populated_cdll):
    assert populated_cdll[0] is populated_cdll.head
    assert populated_cdll[3] is populated_cdll.tail


def test_getitem_single_element():
    ll = CircularDLL(10)

    assert ll[0] is ll.head
    assert ll[0] is ll.tail


@pytest.mark.parametrize("index", [ 4, 10])
def test_getitem_invalid_index(populated_cdll, index):
    with pytest.raises(IndexError):
        _ = populated_cdll[index]


@pytest.mark.parametrize("index", ["1", 1.5, None])
def test_getitem_invalid_index_type(populated_cdll, index):
    with pytest.raises(TypeError):
        _ = populated_cdll[index]


# ============================================================
# ITERATION TESTS
# ============================================================

def test_iteration_empty_list(empty_cdll):
    assert list(empty_cdll) == []


def test_iteration_single_element():
    ll = CircularDLL(10)

    nodes = list(ll)

    assert len(nodes) == 1
    assert nodes[0].val == 10


def test_iteration_multiple_elements(populated_cdll):
    nodes = list(populated_cdll)

    assert [node.val for node in nodes] == [10, 20, 30, 40]


def test_iteration_terminates(populated_cdll):
    from itertools import islice

    nodes = list(islice(iter(populated_cdll), 5))

    assert len(nodes) == 4


def test_iteration_returns_unique_nodes(populated_cdll):
    nodes = list(populated_cdll)

    assert len({id(node) for node in nodes}) == 4


# ============================================================
# EXTEND TESTS
# Deep-copy semantics; source remains unchanged.
# ============================================================

def test_extend_empty_source():
    target = CircularDLL(1, 2, 3)
    source = CircularDLL()

    target.extend(source)

    assert_cdll_invariants(target, [1, 2, 3])
    assert_cdll_invariants(source, [])


def test_extend_empty_target():
    target = CircularDLL()
    source = CircularDLL(1, 2, 3)

    target.extend(source)

    assert_cdll_invariants(target, [1, 2, 3])
    assert_cdll_invariants(source, [1, 2, 3])


def test_extend_both_empty():
    target = CircularDLL()
    source = CircularDLL()

    target.extend(source)

    assert_cdll_invariants(target, [])
    assert_cdll_invariants(source, [])


def test_extend_two_populated_lists():
    target = CircularDLL(1, 2, 3)
    source = CircularDLL(4, 5, 6)

    target.extend(source)

    assert_cdll_invariants(target, [1, 2, 3, 4, 5, 6])
    assert_cdll_invariants(source, [4, 5, 6])


def test_extend_preserves_existing_target_nodes():
    target = CircularDLL(1, 2)
    source = CircularDLL(3, 4)

    old_head = target.head
    old_tail = target.tail

    target.extend(source)

    assert target.head is old_head
    assert target[1] is old_tail


def test_extend_creates_new_nodes():
    target = CircularDLL(1, 2)
    source = CircularDLL(3, 4)

    source_nodes = list(source)

    target.extend(source)

    assert target[2] is not source_nodes[0]
    assert target[3] is not source_nodes[1]


def test_extend_preserves_source_nodes():
    target = CircularDLL(1, 2)
    source = CircularDLL(3, 4)

    old_head = source.head
    old_tail = source.tail

    target.extend(source)

    assert source.head is old_head
    assert source.tail is old_tail

    assert_cdll_invariants(source, [3, 4])


def test_extend_deep_copies_values():
    payload = [1, 2, 3]

    target = CircularDLL()
    source = CircularDLL(payload)

    target.extend(source)

    assert target.head.val == payload
    assert target.head.val is not payload

    assert source.head.val is payload


def test_extend_does_not_share_mutable_values():
    payload = [1, 2, 3]

    target = CircularDLL()
    source = CircularDLL(payload)

    target.extend(source)

    target.head.val.append(99)

    assert source.head.val == [1, 2, 3]
    assert target.head.val == [1, 2, 3, 99]


def test_extend_preserves_circularity():
    target = CircularDLL(1, 2)
    source = CircularDLL(3, 4)

    target.extend(source)

    assert_cdll_invariants(target, [1, 2, 3, 4])
    assert_cdll_invariants(source, [3, 4])


def test_extend_self_is_rejected():
    ll = CircularDLL(1, 2, 3)

    with pytest.raises(ValueError):
        ll.extend(ll)

    assert_cdll_invariants(ll, [1, 2, 3])


def test_extend_invalid_type():
    ll = CircularDLL(1, 2)

    with pytest.raises(TypeError):
        ll.extend([3, 4])

    assert_cdll_invariants(ll, [1, 2])


# ============================================================
# ADDITION TESTS
# Deep-copy semantics.
# ============================================================

def test_add_two_populated_lists():
    ll1 = CircularDLL(1, 2, 3)
    ll2 = CircularDLL(4, 5, 6)

    result = ll1 + ll2

    assert isinstance(result, CircularDLL)

    assert_cdll_invariants(result, [1, 2, 3, 4, 5, 6])
    assert_cdll_invariants(ll1, [1, 2, 3])
    assert_cdll_invariants(ll2, [4, 5, 6])


def test_add_empty_lists():
    ll1 = CircularDLL()
    ll2 = CircularDLL()

    result = ll1 + ll2

    assert_cdll_invariants(result, [])


def test_add_empty_left():
    ll1 = CircularDLL()
    ll2 = CircularDLL(1, 2, 3)

    result = ll1 + ll2

    assert_cdll_invariants(result, [1, 2, 3])


def test_add_empty_right():
    ll1 = CircularDLL(1, 2, 3)
    ll2 = CircularDLL()

    result = ll1 + ll2

    assert_cdll_invariants(result, [1, 2, 3])


def test_add_does_not_share_nodes():
    ll1 = CircularDLL(1, 2)
    ll2 = CircularDLL(3, 4)

    result = ll1 + ll2

    assert result.head is not ll1.head
    assert result[2] is not ll2.head


def test_add_does_not_modify_original_lists():
    ll1 = CircularDLL(1, 2)
    ll2 = CircularDLL(3, 4)

    result = ll1 + ll2

    assert_cdll_invariants(ll1, [1, 2])
    assert_cdll_invariants(ll2, [3, 4])


def test_add_deep_copies_mutable_values():
    ll1 = CircularDLL([1, 2])
    ll2 = CircularDLL([3, 4])

    result = ll1 + ll2

    result.head.val.append(99)

    assert ll1.head.val == [1, 2]
    assert result.head.val == [1, 2, 99]


def test_add_invalid_type():
    ll = CircularDLL(1, 2)

    assert ll.__add__([3, 4]) is NotImplemented


# ============================================================
# MUTATION SEQUENCE TESTS
# ============================================================

def test_append_then_remove():
    ll = CircularDLL()

    ll.append(10)
    ll.append(20)
    ll.append(30)

    ll.remove(1)

    assert_cdll_invariants(ll, [10, 30])


def test_insert_then_pop():
    ll = CircularDLL(10, 20)

    ll.insert(5, 0)
    ll.pop()

    assert_cdll_invariants(ll, [5, 10])


def test_empty_list_can_be_reused():
    ll = CircularDLL(10)

    ll.pop()

    assert_cdll_invariants(ll, [])

    ll.append(20)

    assert_cdll_invariants(ll, [20])


def test_repeated_insert_and_remove():
    ll = CircularDLL()

    for i in range(10):
        ll.insert(i, 0)

    assert_cdll_invariants(ll, list(reversed(range(10))))

    for _ in range(5):
        ll.remove(0)

    assert_cdll_invariants(ll, [4, 3, 2, 1, 0])


def test_extend_then_append():
    ll1 = CircularDLL(1, 2)
    ll2 = CircularDLL(3, 4)

    ll1.extend(ll2)
    ll1.append(5)

    assert_cdll_invariants(ll1, [1, 2, 3, 4, 5])
    assert_cdll_invariants(ll2, [3, 4])


def test_extend_then_remove():
    ll1 = CircularDLL(1, 2)
    ll2 = CircularDLL(3, 4)

    ll1.extend(ll2)
    ll1.remove(2)

    assert_cdll_invariants(ll1, [1, 2, 4])
    assert_cdll_invariants(ll2, [3, 4])


def test_repeated_pop_and_append():
    ll = CircularDLL(1, 2, 3)

    for i in range(4, 10):
        removed = ll.pop()
        assert removed.next is None
        assert removed.prev is None

        ll.append(i)

        assert ll.tail.next is ll.head
        assert ll.head.prev is ll.tail

    assert_cdll_invariants(ll, [1, 2, 9])
