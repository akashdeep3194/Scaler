class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        i = 1
        head = A
        header = None
        if B != 1:
            ret = head
        prev = None
        while head is not None:
            if i >= B and i <= C:
                if i == B:
                    tailer = head
                tmp = head.next
                head.next = prev
                prev = head
                head = tmp
                if i == C:
                    if header is not None:
                        header.next = prev
                    else:
                        ret = prev
                    tailer.next = head
            else:
                header = head
                head = head.next
            i += 1
        return ret


if __name__ == "__main__":
    s = Solution()
    head = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n6 = ListNode(6)
    n7 = ListNode(7)
    head.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    node = head

    while node is not None:
        print(node.val)
        node = node.next

    nh = s.reverseBetween(head, 2, 4)
    node = nh
    while node is not None:
        print(node.val)
        node = node.next
