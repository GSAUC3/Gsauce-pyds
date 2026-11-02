
def assert_sll_invariants(ll):

    nodes = list(ll)

    assert len(nodes) == len(ll)

    if len(ll) == 0:
        assert ll.head is None
        assert ll.tail is None
        return

    assert ll.head is nodes[0]
    assert ll.tail is nodes[-1]
    assert ll.tail.next is None

    for i in range(len(nodes) - 1):
        assert nodes[i].next is nodes[i + 1]


def assert_dll_invariants(ll):

    nodes = list(ll)

    assert len(nodes) == len(ll)

    if len(ll) == 0:
        assert ll.head is None
        assert ll.tail is None
        return

    assert ll.head is nodes[0]
    assert ll.tail is nodes[-1]

    assert ll.head.prev is None
    assert ll.tail.next is None

    for i, node in enumerate(nodes):

        expected_prev = nodes[i - 1] if i > 0 else None
        expected_next = nodes[i + 1] if i < len(nodes) - 1 else None

        assert node.prev is expected_prev
        assert node.next is expected_next
