
import pytest

from ADS.linked_lists import SLL, DLL, CircularSLL, CircularDLL


LIST_CLASSES = [SLL, DLL, CircularSLL, CircularDLL]


@pytest.fixture(params=LIST_CLASSES)
def linked_list(request):
    return request.param(10, 20, 30, 40)


def snapshot(ll):
    """Capture node identities and their links before an operation."""
    return [
        (node, node.next, getattr(node, "prev", None))
        for node in ll
    ]


def assert_unchanged(ll, before):
    """Verify that an invalid operation did not modify the list."""
    after = list(ll)

    assert len(after) == len(before)

    for current, (original, next_node, prev_node) in zip(after, before):
        assert current is original
        assert current.next is next_node

        if hasattr(current, "prev"):
            assert current.prev is prev_node


# --------------------------------------------------
# __getitem__: valid negative indexes
# --------------------------------------------------

@pytest.mark.parametrize(
    "index, expected",
    [
        (-1, 40),
        (-2, 30),
        (-3, 20),
        (-4, 10),
    ],
)
def test_getitem_valid_negative_indexes(linked_list, index, expected):
    assert linked_list[index].val == expected


# --------------------------------------------------
# __getitem__: invalid negative indexes
# --------------------------------------------------

@pytest.mark.parametrize("index", [-5, -6, -100])
def test_getitem_out_of_range_negative_indexes(linked_list, index):
    with pytest.raises(IndexError):
        linked_list[index]


def test_getitem_negative_index_on_empty_list(request):
    for list_cls in LIST_CLASSES:
        ll = list_cls()

        with pytest.raises(IndexError):
            ll[-1]



# --------------------------------------------------
# insert: valid negative indexes
# --------------------------------------------------

@pytest.mark.parametrize(
    "index, expected",
    [
        (-1, [10, 20, 30, 99, 40]),
        (-2, [10, 20, 99, 30, 40]),
        (-3, [10, 99, 20, 30, 40]),
        (-4, [99, 10, 20, 30, 40]),
    ],
)
def test_insert_valid_negative_indexes(linked_list, index, expected):
    linked_list.insert(99, index=index)

    assert [node.val for node in linked_list] == expected
    assert len(linked_list) == 5


# --------------------------------------------------
# insert: invalid negative indexes
# --------------------------------------------------

@pytest.mark.parametrize("index", [-5, -6, -100])
def test_insert_out_of_range_negative_indexes(linked_list, index):
    before = snapshot(linked_list)

    with pytest.raises(IndexError):
        linked_list.insert(99, index=index)

    assert_unchanged(linked_list, before)


# --------------------------------------------------
# insert: negative indexes on empty lists
# --------------------------------------------------

@pytest.mark.parametrize("list_cls", LIST_CLASSES)
def test_insert_negative_index_on_empty_list(list_cls):
    ll = list_cls()

    with pytest.raises(IndexError):
        ll.insert(99, index=-1)

    assert len(ll) == 0
    assert ll.head is None
    assert ll.tail is None


# --------------------------------------------------
# remove: valid negative indexes
# --------------------------------------------------

@pytest.mark.parametrize(
    "index, expected",
    [
        (-1, [10, 20, 30]),
        (-2, [10, 20, 40]),
        (-3, [10, 30, 40]),
        (-4, [20, 30, 40]),
    ],
)
def test_remove_valid_negative_indexes(linked_list, index, expected):
    removed = linked_list.remove(index=index)

    assert [node.val for node in linked_list] == expected
    assert len(linked_list) == 3


# --------------------------------------------------
# remove: invalid negative indexes
# --------------------------------------------------

@pytest.mark.parametrize("index", [-5, -6, -100])
def test_remove_out_of_range_negative_indexes(linked_list, index):
    before = snapshot(linked_list)

    with pytest.raises(IndexError):
        linked_list.remove(index=index)

    assert_unchanged(linked_list, before)


# --------------------------------------------------
# remove: negative indexes on empty lists
# --------------------------------------------------

@pytest.mark.parametrize("list_cls", LIST_CLASSES)
def test_remove_negative_index_on_empty_list(list_cls):
    ll = list_cls()

    with pytest.raises(IndexError):
        ll.remove(index=-1)

    assert len(ll) == 0
    assert ll.head is None
    assert ll.tail is None


# --------------------------------------------------
# Empty lists
# --------------------------------------------------

@pytest.mark.parametrize("list_cls", LIST_CLASSES)
def test_empty_list_rejects_negative_getitem(list_cls):
    ll = list_cls()

    with pytest.raises(IndexError):
        ll[-1]


@pytest.mark.parametrize("list_cls", LIST_CLASSES)
def test_empty_list_rejects_negative_insert(list_cls):
    ll = list_cls()

    with pytest.raises(IndexError):
        ll.insert(99, index=-1)

    assert len(ll) == 0
    assert ll.head is None
    assert ll.tail is None


@pytest.mark.parametrize("list_cls", LIST_CLASSES)
def test_empty_list_rejects_negative_remove(list_cls):
    ll = list_cls()

    with pytest.raises(IndexError):
        ll.remove(index=-1)

    assert len(ll) == 0
    assert ll.head is None
    assert ll.tail is None
