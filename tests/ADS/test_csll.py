
import pytest
from ADS.linked_lists import CircularSLL, SLLNode


@pytest.fixture
def empty_csll():
    return CircularSLL()


@pytest.fixture
def populated_csll():
    return CircularSLL(10, 20, 30, 40)


def assert_csll_invariants(ll, expected):
    """
    Verify all structural invariants of a CircularSLL.
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

    # Circular connection
    assert ll.tail.next is ll.head

    # Traverse exactly size nodes
    current = ll.head
    visited = []

    for _ in range(len(expected)):
        assert current is not None
        visited.append(current.val)
        current = current.next

    # Must return to the head after exactly size steps
    assert current is ll.head

    # Check values
    assert visited == expected

    # Check tail
    assert ll.tail is not None
    assert ll.tail.val == expected[-1]

    # Ensure no premature cycle
    nodes = []
    current = ll.head

    for _ in range(len(expected)):
        assert current not in nodes
        nodes.append(current)
        current = current.next

    assert nodes[-1] is ll.tail

def test_constructor_empty():
    ll = CircularSLL()

    assert_csll_invariants(ll, [])


def test_constructor_single_element():
    ll = CircularSLL(10)

    assert_csll_invariants(ll, [10])


def test_constructor_multiple_elements():
    ll = CircularSLL(10, 20, 30)

    assert_csll_invariants(ll, [10, 20, 30])


def test_constructor_with_none():
    ll = CircularSLL(None)

    assert_csll_invariants(ll, [None])


def test_constructor_preserves_order():
    ll = CircularSLL(5, 10, 15, 20)

    assert_csll_invariants(ll, [5, 10, 15, 20])





def test_append_empty_list(empty_csll):
    empty_csll.append(10)

    assert_csll_invariants(empty_csll, [10])


def test_append_multiple_elements(empty_csll):
    empty_csll.append(10)
    empty_csll.append(20)
    empty_csll.append(30)

    assert_csll_invariants(empty_csll, [10, 20, 30])


def test_append_to_populated_list(populated_csll):
    populated_csll.append(50)

    assert_csll_invariants(
        populated_csll,
        [10, 20, 30, 40, 50]
    )


def test_append_updates_head_and_tail(empty_csll):
    empty_csll.append(10)

    assert empty_csll.head is empty_csll.tail
    assert empty_csll.tail.next is empty_csll.head


def test_append_preserves_head(populated_csll):
    old_head = populated_csll.head

    populated_csll.append(50)

    assert populated_csll.head is old_head
    assert_csll_invariants(populated_csll, [10, 20, 30, 40, 50])


def test_append_updates_tail(populated_csll):
    old_tail = populated_csll.tail

    populated_csll.append(50)

    assert populated_csll.tail is not old_tail
    assert populated_csll.tail.val == 50






def test_insert_into_empty_list(empty_csll):
    empty_csll.insert(10, 0)

    assert_csll_invariants(empty_csll, [10])


def test_insert_at_head(populated_csll):
    populated_csll.insert(5, 0)

    assert_csll_invariants(
        populated_csll,
        [5, 10, 20, 30, 40]
    )


def test_insert_at_middle(populated_csll):
    populated_csll.insert(25, 2)

    assert_csll_invariants(
        populated_csll,
        [10, 20, 25, 30, 40]
    )


def test_insert_at_tail(populated_csll):
    populated_csll.insert(50, 4)

    assert_csll_invariants(
        populated_csll,
        [10, 20, 30, 40, 50]
    )


def test_insert_at_head_updates_tail(empty_csll):
    empty_csll.insert(10, 0)

    assert empty_csll.head is empty_csll.tail


def test_insert_at_tail_updates_tail(populated_csll):
    populated_csll.insert(50, 4)

    assert populated_csll.tail.val == 50
    assert populated_csll.tail.next is populated_csll.head


def test_insert_preserves_existing_nodes(populated_csll):
    old_nodes = [populated_csll[i] for i in range(4)]

    populated_csll.insert(25, 2)

    assert populated_csll[0] is old_nodes[0]
    assert populated_csll[1] is old_nodes[1]
    assert populated_csll[3] is old_nodes[2]
    assert populated_csll[4] is old_nodes[3]


def test_insert_out_of_bounds(populated_csll):
    with pytest.raises(IndexError):
        populated_csll.insert(50, 5)


def test_insert_negative_index(populated_csll):
    with pytest.raises(IndexError):
        populated_csll.insert(50, -1)


def test_insert_invalid_index_type(populated_csll):
    with pytest.raises(TypeError):
        populated_csll.insert(50, "2")








def test_pop_empty_list(empty_csll):
    with pytest.raises(IndexError):
        empty_csll.pop()


def test_pop_single_element():
    ll = CircularSLL(10)

    removed = ll.pop()

    assert removed.val == 10
    assert removed.next is None

    assert_csll_invariants(ll, [])


def test_pop_multiple_elements(populated_csll):
    removed = populated_csll.pop()

    assert removed.val == 40
    assert removed.next is None

    assert_csll_invariants(
        populated_csll,
        [10, 20, 30]
    )


def test_pop_updates_tail(populated_csll):
    old_tail = populated_csll.tail

    populated_csll.pop()

    assert populated_csll.tail is not old_tail
    assert populated_csll.tail.val == 30


def test_pop_preserves_head(populated_csll):
    old_head = populated_csll.head

    populated_csll.pop()

    assert populated_csll.head is old_head


def test_pop_updates_circular_connection(populated_csll):
    populated_csll.pop()

    assert populated_csll.tail.next is populated_csll.head


def test_pop_until_empty(populated_csll):
    for _ in range(4):
        populated_csll.pop()

    assert_csll_invariants(populated_csll, [])







def test_remove_head(populated_csll):
    old_head = populated_csll.head

    removed = populated_csll.remove(0)

    assert removed is old_head
    assert removed.val == 10
    assert removed.next is None

    assert_csll_invariants(
        populated_csll,
        [20, 30, 40]
    )


def test_remove_middle(populated_csll):
    removed = populated_csll.remove(1)

    assert removed.val == 20
    assert removed.next is None

    assert_csll_invariants(
        populated_csll,
        [10, 30, 40]
    )


def test_remove_tail(populated_csll):
    old_tail = populated_csll.tail

    removed = populated_csll.remove(3)

    assert removed is old_tail
    assert removed.val == 40
    assert removed.next is None

    assert_csll_invariants(
        populated_csll,
        [10, 20, 30]
    )


def test_remove_only_element():
    ll = CircularSLL(10)

    removed = ll.remove(0)

    assert removed.val == 10
    assert removed.next is None

    assert_csll_invariants(ll, [])


def test_remove_from_empty_list(empty_csll):
    with pytest.raises(IndexError):
        empty_csll.remove(0)


def test_remove_negative_index(populated_csll):
    with pytest.raises(IndexError):
        populated_csll.remove(-1)


def test_remove_out_of_bounds(populated_csll):
    with pytest.raises(IndexError):
        populated_csll.remove(4)


def test_remove_invalid_index_type(populated_csll):
    with pytest.raises(TypeError):
        populated_csll.remove("1")


def test_remove_all_elements(populated_csll):
    for _ in range(4):
        populated_csll.remove(0)

    assert_csll_invariants(populated_csll, [])


import pytest


def test_extend_empty_source():
    target = CircularSLL(1, 2, 3)
    source = CircularSLL()

    target.extend(source)

    assert_csll_invariants(target, [1, 2, 3])
    assert_csll_invariants(source, [])


def test_extend_empty_target():
    target = CircularSLL()
    source = CircularSLL(1, 2, 3)

    target.extend(source)

    assert_csll_invariants(target, [1, 2, 3])
    assert_csll_invariants(source, [1, 2, 3])


def test_extend_both_empty():
    target = CircularSLL()
    source = CircularSLL()

    target.extend(source)

    assert_csll_invariants(target, [])
    assert_csll_invariants(source, [])


def test_extend_two_populated_lists():
    target = CircularSLL(1, 2, 3)
    source = CircularSLL(4, 5, 6)

    target.extend(source)

    assert_csll_invariants(target, [1, 2, 3, 4, 5, 6])
    assert_csll_invariants(source, [4, 5, 6])


def test_extend_preserves_existing_target_nodes():
    target = CircularSLL(1, 2)
    source = CircularSLL(3, 4)

    old_head = target.head
    old_tail = target.tail

    target.extend(source)

    assert target.head is old_head
    assert target.tail is not old_tail
    assert target[1] is old_tail


def test_extend_creates_new_nodes():
    target = CircularSLL(1, 2)
    source = CircularSLL(3, 4)

    source_nodes = [node for node in source]

    target.extend(source)

    target_nodes = [node for node in target]

    assert target_nodes[2] is not source_nodes[0]
    assert target_nodes[3] is not source_nodes[1]


def test_extend_preserves_source_nodes():
    target = CircularSLL(1, 2)
    source = CircularSLL(3, 4)

    source_head = source.head
    source_tail = source.tail

    target.extend(source)

    assert source.head is source_head
    assert source.tail is source_tail
    assert_csll_invariants(source, [3, 4])

def test_extend_deep_copies_mutable_values():
    payload = [1, 2, 3]

    target = CircularSLL()
    source = CircularSLL(payload)

    target.extend(source)

    target.head.val.append(4)

    assert source.head.val == [1, 2, 3]
    assert target.head.val == [1, 2, 3, 4]


def test_extend_does_not_modify_source_values():
    payload = [1, 2, 3]

    target = CircularSLL()
    source = CircularSLL(payload)

    target.extend(source)

    source.head.val.append(4)

    assert target.head.val == [1, 2, 3]
    assert source.head.val == [1, 2, 3, 4]


def test_extend_deep_copies_values():
    payload = [1, 2, 3]

    target = CircularSLL()
    source = CircularSLL(payload)

    target.extend(source)

    assert target.head.val == payload
    assert target.head.val is not payload

    assert source.head.val is payload

def test_extend_preserves_circularity():
    target = CircularSLL(1, 2)
    source = CircularSLL(3, 4)

    target.extend(source)

    assert target.tail.next is target.head
    assert source.tail.next is source.head


def test_extend_self():
    ll = CircularSLL(1, 2, 3)
    with pytest.raises(ValueError):
        ll.extend(ll)

   

def test_extend_invalid_type():
    ll = CircularSLL(1, 2)

    with pytest.raises(TypeError):
        ll.extend([3, 4])

    assert_csll_invariants(ll, [1, 2])




def test_getitem_first(populated_csll):
    assert populated_csll[0].val == 10


def test_getitem_middle(populated_csll):
    assert populated_csll[2].val == 30


def test_getitem_last(populated_csll):
    assert populated_csll[3].val == 40


def test_getitem_returns_node(populated_csll):
    node = populated_csll[0]

    assert node is populated_csll.head


def test_getitem_out_of_bounds(populated_csll):
    with pytest.raises(IndexError):
        _ = populated_csll[4]


def test_getitem_negative_index(populated_csll):
    with pytest.raises(IndexError):
        _ = populated_csll[-1]


def test_getitem_invalid_type(populated_csll):
    with pytest.raises(TypeError):
        _ = populated_csll["1"]


def test_getitem_single_element():
    ll = CircularSLL(10)

    assert ll[0] is ll.head
    assert ll[0] is ll.tail




from itertools import islice


def test_iteration_empty_list(empty_csll):
    assert list(empty_csll) == []


def test_iteration_single_element():
    ll = CircularSLL(10)

    result = [node.val for node in ll]

    assert result == [10]


def test_iteration_multiple_elements(populated_csll):
    result = [node.val for node in populated_csll]

    assert result == [10, 20, 30, 40]


def test_iteration_terminates(populated_csll):
    result = list(islice(iter(populated_csll), 5))

    assert len(result) == 4


def test_iteration_returns_nodes(populated_csll):
    for node in populated_csll:
        assert hasattr(node, "val")
        assert hasattr(node, "next")


def test_iteration_does_not_repeat_head(populated_csll):
    nodes = list(islice(iter(populated_csll), 5))

    assert len(nodes) == 4
    assert len({id(node) for node in nodes}) == 4







# def test_add_two_populated_lists():
#     ll1 = CircularSLL(1, 2, 3)
#     ll2 = CircularSLL(4, 5, 6)

#     result = ll1 + ll2

#     assert_csll_invariants(result, [1, 2, 3, 4, 5, 6])

#     assert_csll_invariants(ll1, [1, 2, 3])
#     assert_csll_invariants(ll2, [4, 5, 6])


# def test_add_empty_lists():
#     ll1 = CircularSLL()
#     ll2 = CircularSLL()

#     result = ll1 + ll2

#     assert_csll_invariants(result, [])


# def test_add_empty_left():
#     ll1 = CircularSLL()
#     ll2 = CircularSLL(1, 2, 3)

#     result = ll1 + ll2

#     assert_csll_invariants(result, [1, 2, 3])


# def test_add_empty_right():
#     ll1 = CircularSLL(1, 2, 3)
#     ll2 = CircularSLL()

#     result = ll1 + ll2

#     assert_csll_invariants(result, [1, 2, 3])


# def test_add_does_not_share_nodes():
#     ll1 = CircularSLL(1, 2)
#     ll2 = CircularSLL(3, 4)

#     result = ll1 + ll2

#     assert result.head is not ll1.head
#     assert result.tail is not ll2.tail


# def test_add_does_not_modify_original_lists():
#     ll1 = CircularSLL(1, 2)
#     ll2 = CircularSLL(3, 4)

#     result = ll1 + ll2

#     assert_csll_invariants(ll1, [1, 2])
#     assert_csll_invariants(ll2, [3, 4])


# def test_add_deep_copies_mutable_values():
#     ll1 = CircularSLL([1, 2])
#     ll2 = CircularSLL([3, 4])

#     result = ll1 + ll2

#     result.head.val.append(99)

#     assert ll1.head.val == [1, 2]
#     assert result.head.val == [1, 2, 99]


# def test_add_invalid_type():
#     ll = CircularSLL(1, 2)

#     with pytest.raises(TypeError):
#         _ = ll + [3, 4]





def test_append_then_remove():
    ll = CircularSLL()

    ll.append(10)
    ll.append(20)
    ll.append(30)

    ll.remove(1)

    assert_csll_invariants(ll, [10, 30])


def test_insert_then_pop():
    ll = CircularSLL(10, 20)

    ll.insert(5, 0)
    ll.pop()

    assert_csll_invariants(ll, [5, 10])


def test_empty_list_can_be_reused():
    ll = CircularSLL(10)

    ll.pop()

    assert_csll_invariants(ll, [])

    ll.append(20)

    assert_csll_invariants(ll, [20])


def test_repeated_insert_and_remove():
    ll = CircularSLL()

    for i in range(10):
        ll.insert(i, 0)

    assert_csll_invariants(ll, list(reversed(range(10))))

    for _ in range(5):
        ll.remove(0)

    assert_csll_invariants(ll, [4, 3, 2, 1, 0])


def test_extend_then_append():
    ll1 = CircularSLL(1, 2)
    ll2 = CircularSLL(3, 4)

    ll1.extend(ll2)
    ll1.append(5)

    assert_csll_invariants(ll1, [1, 2, 3, 4, 5])
    assert_csll_invariants(ll2, [3,4])


def test_extend_then_remove():
    ll1 = CircularSLL(1, 2)
    ll2 = CircularSLL(3, 4)

    ll1.extend(ll2)
    ll1.remove(2)

    assert_csll_invariants(ll1, [1, 2, 4])
    assert_csll_invariants(ll2, [3,4])




