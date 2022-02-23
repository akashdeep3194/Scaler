# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list

    def merge_sorted(self, h1, h2):
        if h1.val <= h2.val:
            pass
        else:
            h1, h2 = h2, h1
        head = h1
        while h1.next is not None and h2 is not None:
            if h1.next.val >= h2.val:
                tmp = h1.next
                h1.next = h2
                h2 = tmp
                h1 = h1.next
            else:
                h1 = h1.next
        h1.next = h2
        return head

    def sortList(self, A):
        if A is None or A.next is None:
            return A

        slow = A
        fast = A
        pslow = None
        while fast is not None and fast.next is not None:
            pslow = slow
            fast = fast.next.next
            slow = slow.next
        if fast is None:
            mid = pslow
        else:
            mid = slow
        h2 = mid.next
        mid.next = None
        h1 = A
        h1 = self.sortList(h1)
        h2 = self.sortList(h2)

        head = self.merge_sorted(h1, h2)
        return head


def printll(n):
    while n is not None:
        print(n.val, end="->")
        n = n.next
    print()


if __name__ == "__main__":
    s = Solution()
    A1 = ListNode(10)
    A2 = ListNode(15)
    A3 = ListNode(30)
    A4 = ListNode(6)
    A5 = ListNode(9)
    A6 = ListNode(32)
    A7 = ListNode(60)
    A8 = ListNode(1)
    A1.next = A2
    A2.next = A3
    A3.next = A4
    A4.next = A5
    A5.next = A6
    A6.next = A7
    A7.next = A8

    ans = s.sortList(A1)
    printll(ans)
