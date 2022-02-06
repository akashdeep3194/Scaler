# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def revLL(self, head, prev, k):
        i = 0
        tail = head
        while head is not None and i < k:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
            i += 1
        return prev, head, tail

    def reverseList(self, A, B):
        prev = None
        head = A
        tailer = None
        i = 0
        while head is not None:
            prev, head, tail = self.revLL(head, prev, B)
            if head is None:
                tail.next = None
            if i == 0:
                ret = prev
                i += 1
            if tailer is not None:
                tailer.next = prev
            tailer = tail
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

    nh = s.reverseList(head, 2)
    node = nh
    while node is not None:
        print(node.val)
        node = node.next
