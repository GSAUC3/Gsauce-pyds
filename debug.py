class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head

        new_head = self.reverseList(head.next)

        head.next.next = head
        head.next = None
        

        return new_head


def printnodes(head):
    i = head
    while i:
        print(i.val, end=' -> ')
        i=i.next
    print('None')

if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    printnodes(head)
    sol = Solution()
    h = sol.reverseList(head=head)
    printnodes(h)
