
import pytest
from ADS.linked_lists import SLL, SLLNode


# ============================================================
# 1. CONSTRUCTION
# ============================================================

def test_empty_sll():
    ll = SLL()

    assert len(ll) == 0
    assert ll.size == 0
    assert ll.head is None
    assert ll.tail is None


def test_single_element_constructor():
    ll = SLL(10)

    assert len(ll) == 1
    assert ll.head.val == 10
    assert ll.tail.val == 10
    assert ll.head is ll.tail


def test_multiple_element_constructor():
    ll = SLL(10, 20, 30)

    assert len(ll) == 3
    assert [node.val for node in ll] == [10, 20, 30]


def test_constructor_preserves_order():
    ll = SLL(1, 2, 3, 4, 5)

    assert [node.val for node in ll] == [1, 2, 3, 4, 5]


# ============================================================
# 2. NODE
# ============================================================

def test_sll_node_initialization():
    node = SLLNode(10)

    assert node.val == 10
    assert node.next is None
    assert node.dtype is int


def test_sll_node_linking():
    second = SLLNode(20)
    first = SLLNode(10, second)

    assert first.next is second
    assert first.next.val == 20


def test_sll_node_string_representation():
    node = SLLNode(10)

    assert str(node) == "Node(10)"
    assert repr(node) == "Node(10)"


# ============================================================
# 3. PROPERTIES AND SPECIAL METHODS
# ============================================================

def test_size_property():
    ll = SLL(1, 2, 3)

    assert ll.size == 3


def test_len():
    ll = SLL(1, 2, 3, 4)

    assert len(ll) == 4


def test_string_representation():
    ll = SLL(1, 2, 3)

    assert str(ll) == "LinkedList([1, 2, 3])"


def test_repr():
    ll = SLL(1, 2, 3)

    assert repr(ll) == "Node(1) -> Node(2) -> Node(3)"


def test_empty_string_representation():
    ll = SLL()

    assert str(ll) == "LinkedList([])"
    assert repr(ll) == ""


# ============================================================
# 4. ITERATION
# ============================================================

def test_iteration():
    ll = SLL(1, 2, 3)

    result = [node.val for node in ll]

    assert result == [1, 2, 3]


def test_iteration_empty_list():
    ll = SLL()

    assert list(ll) == []


def test_iteration_returns_nodes():
    ll = SLL(1, 2, 3)

    nodes = list(ll)

    assert all(isinstance(node, SLLNode) for node in nodes)


def test_iteration_preserves_node_identity():
    ll = SLL(1, 2, 3)

    nodes = list(ll)

    assert nodes[0] is ll.head
    assert nodes[-1] is ll.tail


# ============================================================
# 5. INDEXING
# ============================================================

def test_getitem_first_element():
    ll = SLL(10, 20, 30)

    assert ll[0].val == 10


def test_getitem_middle_element():
    ll = SLL(10, 20, 30)

    assert ll[1].val == 20


def test_getitem_last_element():
    ll = SLL(10, 20, 30)

    assert ll[2].val == 30


def test_getitem_returns_node():
    ll = SLL(10, 20, 30)

    assert isinstance(ll[1], SLLNode)


def test_getitem_negative_index():
    ll = SLL(10, 20, 30)

    with pytest.raises(IndexError):
        ll[-1]


def test_getitem_out_of_range():
    ll = SLL(10, 20, 30)

    with pytest.raises(IndexError):
        ll[3]


def test_getitem_empty_list():
    ll = SLL()

    with pytest.raises(IndexError):
        ll[0]


# ============================================================
# 6. APPEND
# ============================================================

def test_append_to_empty_list():
    ll = SLL()

    ll.append(10)

    assert len(ll) == 1
    assert ll.head.val == 10
    assert ll.tail.val == 10
    assert ll.head is ll.tail


def test_append_multiple_elements():
    ll = SLL()

    for value in [10, 20, 30]:
        ll.append(value)

    assert [node.val for node in ll] == [10, 20, 30]
    assert ll.tail.val == 30
    assert len(ll) == 3


def test_append_updates_tail():
    ll = SLL(10, 20)

    old_tail = ll.tail

    ll.append(30)

    assert old_tail.next is ll.tail
    assert ll.tail.val == 30
    assert ll.tail.next is None


def test_append_updates_size():
    ll = SLL(10)

    ll.append(20)

    assert ll.size == 2


def test_append_none_value():
    ll = SLL()

    ll.append(None)

    assert len(ll) == 1
    assert ll.head.val is None


# ============================================================
# 7. ADD FRONT
# ============================================================

def test_add_front_to_empty_list():
    ll = SLL()

    ll.add_front(10)

    assert ll.head.val == 10
    assert ll.tail.val == 10
    assert len(ll) == 1


def test_add_front_to_non_empty_list():
    ll = SLL(20, 30)

    ll.add_front(10)

    assert [node.val for node in ll] == [10, 20, 30]


def test_add_front_updates_head():
    ll = SLL(20, 30)

    old_head = ll.head

    ll.add_front(10)

    assert ll.head.val == 10
    assert ll.head.next is old_head


def test_add_front_does_not_change_tail():
    ll = SLL(20, 30)

    old_tail = ll.tail

    ll.add_front(10)

    assert ll.tail is old_tail


def test_add_front_updates_size():
    ll = SLL(20, 30)

    ll.add_front(10)

    assert len(ll) == 3


# ============================================================
# 8. INSERT
# ============================================================

def test_insert_at_beginning():
    ll = SLL(20, 30)

    ll.insert(10)

    assert [node.val for node in ll] == [10, 20, 30]


def test_insert_at_middle():
    ll = SLL(10, 30)

    ll.insert(20, 1)

    assert [node.val for node in ll] == [10, 20, 30]


def test_insert_at_end():
    ll = SLL(10, 20)

    ll.insert(30, 2)

    assert [node.val for node in ll] == [10, 20, 30]


def test_insert_into_empty_list():
    ll = SLL()

    ll.insert(10, 0)

    assert len(ll) == 1
    assert ll.head.val == 10
    assert ll.tail.val == 10


def test_insert_updates_tail():
    ll = SLL(10, 20)

    ll.insert(30, 2)

    assert ll.tail.val == 30
    assert ll.tail.next is None


@pytest.mark.parametrize("index", [-1, -2, 4, 10])
def test_insert_invalid_index(index):
    ll = SLL(10, 20, 30)

    with pytest.raises(IndexError):
        ll.insert(99, index)


# ============================================================
# 9. REMOVE
# ============================================================

def test_remove_first_element():
    ll = SLL(10, 20, 30)

    removed = ll.remove(0)

    assert removed.val == 10
    assert [node.val for node in ll] == [20, 30]


def test_remove_middle_element():
    ll = SLL(10, 20, 30)

    removed = ll.remove(1)

    assert removed.val == 20
    assert [node.val for node in ll] == [10, 30]


def test_remove_last_element():
    ll = SLL(10, 20, 30)

    removed = ll.remove(2)

    assert removed.val == 30
    assert [node.val for node in ll] == [10, 20]


def test_remove_only_element():
    ll = SLL(10)

    removed = ll.remove(0)

    assert removed.val == 10
    assert len(ll) == 0
    assert ll.head is None
    assert ll.tail is None


def test_remove_updates_size():
    ll = SLL(10, 20, 30)

    ll.remove(1)

    assert len(ll) == 2


def test_remove_updates_tail():
    ll = SLL(10, 20, 30)

    ll.remove(2)

    assert ll.tail.val == 20
    assert ll.tail.next is None


@pytest.mark.parametrize("index", [-1, 3, 10])
def test_remove_invalid_index(index):
    ll = SLL(10, 20, 30)

    with pytest.raises(IndexError):
        ll.remove(index)


def test_remove_from_empty_list():
    ll = SLL()

    with pytest.raises(IndexError):
        ll.remove(0)


# ============================================================
# 10. POP
# ============================================================

def test_pop_from_empty_list():
    ll = SLL()

    with pytest.raises(IndexError):
        ll.pop()


def test_pop_single_element():
    ll = SLL(10)

    removed = ll.pop()

    assert removed.val == 10
    assert len(ll) == 0
    assert ll.head is None
    assert ll.tail is None


def test_pop_multiple_elements():
    ll = SLL(10, 20, 30)

    removed = ll.pop()

    assert removed.val == 30
    assert [node.val for node in ll] == [10, 20]


def test_pop_updates_tail():
    ll = SLL(10, 20, 30)

    ll.pop()

    assert ll.tail.val == 20
    assert ll.tail.next is None


def test_pop_updates_size():
    ll = SLL(10, 20, 30)

    ll.pop()

    assert len(ll) == 2


# ============================================================
# 11. EXTEND
# ============================================================

def test_extend_non_empty_lists():
    ll1 = SLL(1, 2)
    ll2 = SLL(3, 4)

    ll1.extend(ll2)

    assert [node.val for node in ll1] == [1, 2, 3, 4]
    assert len(ll1) == 4


def test_extend_empty_destination():
    ll1 = SLL()
    ll2 = SLL(1, 2, 3)

    ll1.extend(ll2)

    assert [node.val for node in ll1] == [1, 2, 3]
    assert len(ll1) == 3


def test_extend_empty_source():
    ll1 = SLL(1, 2)
    ll2 = SLL()

    ll1.extend(ll2)

    assert [node.val for node in ll1] == [1, 2]
    assert len(ll1) == 2


def test_extend_both_empty():
    ll1 = SLL()
    ll2 = SLL()

    ll1.extend(ll2)

    assert len(ll1) == 0
    assert ll1.head is None
    assert ll1.tail is None


def test_extend_rejects_self():
    ll = SLL(1, 2, 3)

    with pytest.raises(ValueError):
        ll.extend(ll)


# ============================================================
# 12. CONCATENATION
# ============================================================

def test_add_two_non_empty_lists():
    ll1 = SLL(1, 2)
    ll2 = SLL(3, 4)

    result = ll1 + ll2

    assert [node.val for node in result] == [1, 2, 3, 4]


def test_add_empty_lists():
    ll1 = SLL()
    ll2 = SLL()

    result = ll1 + ll2

    assert len(result) == 0


def test_add_empty_left_list():
    ll1 = SLL()
    ll2 = SLL(1, 2)

    result = ll1 + ll2

    assert [node.val for node in result] == [1, 2]


def test_add_empty_right_list():
    ll1 = SLL(1, 2)
    ll2 = SLL()

    result = ll1 + ll2

    assert [node.val for node in result] == [1, 2]


def test_add_does_not_modify_original_lists():
    ll1 = SLL(1, 2)
    ll2 = SLL(3, 4)

    result = ll1 + ll2

    assert [node.val for node in ll1] == [1, 2]
    assert [node.val for node in ll2] == [3, 4]


def test_add_creates_new_nodes():
    ll1 = SLL(1, 2)
    ll2 = SLL(3, 4)

    result = ll1 + ll2

    original_nodes = list(ll1) + list(ll2)
    result_nodes = list(result)

    assert all(
        new_node is not old_node
        for new_node in result_nodes
        for old_node in original_nodes
    )


def test_add_rejects_non_sll():
    ll = SLL(1, 2)

    with pytest.raises(TypeError):
        _ = ll + [3, 4]


# def test_add_deep_copies_mutable_values():
#     ll1 = SLL([1, 2])
#     ll2 = SLL([3, 4])

#     result = ll1 + ll2

#     result.head.val.append(99)

#     assert ll1.head.val == [1, 2]


# ============================================================
# 13. POINTER INTEGRITY
# ============================================================

def test_all_next_pointers_are_correct():
    ll = SLL(1, 2, 3)

    nodes = list(ll)

    assert nodes[0].next is nodes[1]
    assert nodes[1].next is nodes[2]
    assert nodes[2].next is None


def test_head_and_tail_invariants():
    ll = SLL(1, 2, 3)

    assert ll.head is not None
    assert ll.tail is not None
    assert ll.tail.next is None


def test_single_node_invariants():
    ll = SLL(10)

    assert ll.head is ll.tail
    assert ll.head.next is None
    assert len(ll) == 1


def test_empty_list_invariants_after_pop():
    ll = SLL(10)

    ll.pop()

    assert ll.head is None
    assert ll.tail is None
    assert len(ll) == 0
