
import pytest
from ADS.linked_lists import DLL, DLLNode


# ============================================================
# 1. CONSTRUCTION
# ============================================================

def test_empty_dll():
    ll = DLL()

    assert len(ll) == 0
    assert ll.size == 0
    assert ll.head is None
    assert ll.tail is None


def test_single_element_constructor():
    ll = DLL(10)

    assert len(ll) == 1
    assert ll.head.val == 10
    assert ll.tail.val == 10
    assert ll.head is ll.tail


def test_multiple_element_constructor():
    ll = DLL(10, 20, 30)

    assert len(ll) == 3
    assert [node.val for node in ll] == [10, 20, 30]


def test_constructor_preserves_order():
    ll = DLL(1, 2, 3, 4, 5)

    assert [node.val for node in ll] == [1, 2, 3, 4, 5]


# ============================================================
# 2. NODE
# ============================================================

def test_dll_node_initialization():
    node = DLLNode(10)

    assert node.val == 10
    assert node.next is None
    assert node.prev is None


def test_dll_node_forward_linking():
    second = DLLNode(20)
    first = DLLNode(10, next_node=second)

    assert first.next is second


def test_dll_node_backward_linking():
    first = DLLNode(10)
    second = DLLNode(20, prev_node=first)

    assert second.prev is first


def test_dll_node_bidirectional_linking():
    first = DLLNode(10)
    second = DLLNode(20, prev_node=first)

    first.next = second

    assert first.next is second
    assert second.prev is first


def test_dll_node_string_representation():
    node = DLLNode(10)

    assert str(node) == "10"


def test_dll_node_repr():
    node = DLLNode(10)

    assert repr(node) == "Node(None) <=> Node(10) <=> Node(None)"


def test_dll_node_repr_with_neighbours():
    first = DLLNode(10)
    middle = DLLNode(20, prev_node=first)
    last = DLLNode(30, prev_node=middle)

    first.next = middle
    middle.next = last

    assert repr(middle) == "Node(10) <=> Node(20) <=> Node(30)"


# ============================================================
# 3. PROPERTIES AND SPECIAL METHODS
# ============================================================

def test_size_property():
    ll = DLL(1, 2, 3)

    assert ll.size == 3


def test_len():
    ll = DLL(1, 2, 3, 4)

    assert len(ll) == 4


def test_string_representation():
    ll = DLL(1, 2, 3)

    assert str(ll) == "LinkedList([1, 2, 3])"


def test_repr():
    ll = DLL(1, 2, 3)

    assert repr(ll) == "1 <=> 2 <=> 3"


def test_empty_string_representation():
    ll = DLL()

    assert str(ll) == "LinkedList([])"
    assert repr(ll) == ""


# ============================================================
# 4. ITERATION
# ============================================================

def test_iteration():
    ll = DLL(1, 2, 3)

    assert [node.val for node in ll] == [1, 2, 3]


def test_iteration_empty_list():
    ll = DLL()

    assert list(ll) == []


def test_iteration_returns_nodes():
    ll = DLL(1, 2, 3)

    nodes = list(ll)

    assert all(isinstance(node, DLLNode) for node in nodes)


def test_iteration_preserves_node_identity():
    ll = DLL(1, 2, 3)

    nodes = list(ll)

    assert nodes[0] is ll.head
    assert nodes[-1] is ll.tail


# ============================================================
# 5. APPEND
# ============================================================

def test_append_to_empty_list():
    ll = DLL()

    ll.append(10)

    assert len(ll) == 1
    assert ll.head.val == 10
    assert ll.tail.val == 10
    assert ll.head is ll.tail


def test_append_multiple_elements():
    ll = DLL()

    for value in [10, 20, 30]:
        ll.append(value)

    assert [node.val for node in ll] == [10, 20, 30]
    assert len(ll) == 3


def test_append_updates_tail():
    ll = DLL(10, 20)

    old_tail = ll.tail

    ll.append(30)

    assert ll.tail.val == 30
    assert old_tail.next is ll.tail


def test_append_updates_previous_pointer():
    ll = DLL(10, 20)

    old_tail = ll.tail

    ll.append(30)

    assert ll.tail.prev is old_tail


def test_append_updates_size():
    ll = DLL(10, 20)

    ll.append(30)

    assert ll.size == 3


def test_append_preserves_head():
    ll = DLL(10, 20)

    old_head = ll.head

    ll.append(30)

    assert ll.head is old_head


def test_append_none_value():
    ll = DLL()

    ll.append(None)

    assert len(ll) == 1
    assert ll.head.val is None


# ============================================================
# 6. POP
# ============================================================

def test_pop_from_empty_list():
    ll = DLL()

    with pytest.raises(IndexError):
        ll.pop()


def test_pop_single_element():
    ll = DLL(10)

    removed = ll.pop()

    assert removed.val == 10
    assert len(ll) == 0
    assert ll.head is None
    assert ll.tail is None


def test_pop_two_elements():
    ll = DLL(10, 20)

    removed = ll.pop()

    assert removed.val == 20
    assert ll.head.val == 10
    assert ll.tail.val == 10
    assert len(ll) == 1


def test_pop_multiple_elements():
    ll = DLL(10, 20, 30, 40)

    removed = ll.pop()

    assert removed.val == 40
    assert [node.val for node in ll] == [10, 20, 30]


def test_pop_updates_tail():
    ll = DLL(10, 20, 30)

    ll.pop()

    assert ll.tail.val == 20


def test_pop_updates_previous_pointer():
    ll = DLL(10, 20, 30)

    ll.pop()

    assert ll.tail.prev.val == 10


def test_pop_updates_new_tail_next():
    ll = DLL(10, 20, 30)

    ll.pop()

    assert ll.tail.next is None


def test_pop_updates_size():
    ll = DLL(10, 20, 30)

    ll.pop()

    assert len(ll) == 2
    assert ll.size == 2


def test_pop_detaches_removed_node():
    ll = DLL(10, 20, 30)

    removed = ll.pop()

    assert removed.next is None
    assert removed.prev is None


def test_pop_until_empty():
    ll = DLL(10, 20, 30)

    ll.pop()
    ll.pop()
    ll.pop()

    assert len(ll) == 0
    assert ll.head is None
    assert ll.tail is None


# ============================================================
# 7. POINTER INTEGRITY
# ============================================================

def test_head_previous_is_none():
    ll = DLL(10, 20, 30)

    assert ll.head.prev is None


def test_tail_next_is_none():
    ll = DLL(10, 20, 30)

    assert ll.tail.next is None


def test_forward_links():
    ll = DLL(10, 20, 30)

    first, second, third = list(ll)

    assert first.next is second
    assert second.next is third
    assert third.next is None


def test_backward_links():
    ll = DLL(10, 20, 30)

    first, second, third = list(ll)

    assert third.prev is second
    assert second.prev is first
    assert first.prev is None


def test_bidirectional_links():
    ll = DLL(10, 20, 30)

    first, second, third = list(ll)

    assert first.next.prev is first
    assert second.next.prev is second
    assert third.prev.next is third


def test_all_nodes_have_correct_neighbours():
    ll = DLL(10, 20, 30, 40, 50)

    nodes = list(ll)

    for i, node in enumerate(nodes):

        expected_prev = nodes[i - 1] if i > 0 else None
        expected_next = nodes[i + 1] if i < len(nodes) - 1 else None

        assert node.prev is expected_prev
        assert node.next is expected_next


def test_single_node_pointer_invariants():
    ll = DLL(10)

    assert ll.head is ll.tail
    assert ll.head.prev is None
    assert ll.head.next is None


def test_pointer_integrity_after_multiple_appends():
    ll = DLL()

    for value in range(10):
        ll.append(value)

    nodes = list(ll)

    for i in range(len(nodes) - 1):
        assert nodes[i].next is nodes[i + 1]
        assert nodes[i + 1].prev is nodes[i]


def test_pointer_integrity_after_multiple_pops():
    ll = DLL(1, 2, 3, 4, 5)

    ll.pop()
    ll.pop()

    nodes = list(ll)

    assert [node.val for node in nodes] == [1, 2, 3]

    for i in range(len(nodes) - 1):
        assert nodes[i].next is nodes[i + 1]
        assert nodes[i + 1].prev is nodes[i]

    assert ll.head.prev is None
    assert ll.tail.next is None


# ============================================================
# 8. MIXED OPERATIONS
# ============================================================

def test_append_and_pop_sequence():
    ll = DLL()

    ll.append(10)
    ll.append(20)
    ll.pop()
    ll.append(30)

    assert [node.val for node in ll] == [10, 30]
    assert len(ll) == 2


def test_repeated_append_and_pop():
    ll = DLL()

    for i in range(100):
        ll.append(i)

    for i in range(50):
        ll.pop()

    assert len(ll) == 50
    assert ll.head.val == 0
    assert ll.tail.val == 49

    nodes = list(ll)

    for i in range(len(nodes) - 1):
        assert nodes[i].next.prev is nodes[i]


def test_empty_list_can_be_reused():
    ll = DLL(10)

    ll.pop()
    ll.append(20)

    assert len(ll) == 1
    assert ll.head is ll.tail
    assert ll.head.val == 20
    assert ll.head.prev is None
    assert ll.head.next is None
