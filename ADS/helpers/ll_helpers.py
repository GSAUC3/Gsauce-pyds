

def print_linked_list(head, val:bool = False):
    i = head
    while i:
        if val:
            print(i.val, end='  ')
        else:
            print(i, end=' ')

        i = i.next


def reverse_linked_list(head):
    pass

