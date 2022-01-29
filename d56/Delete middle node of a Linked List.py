# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        head = A
        mid = A
        prev = A
        while head is not None and head.next is not None:

            head = (head.next).next
            if head is not None and head.next is not None:
                mid = mid.next
        if mid.next is None:
            return None
        else:
            mid.next = mid.next.next
        return A
