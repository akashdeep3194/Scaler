# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        if A.val <= B.val:
            smallhead = A
            bighead = B
        else:
            smallhead = B
            bighead = A
        header = smallhead
        while smallhead.next is not None:
            if smallhead.next.val <= bighead.val:
                smallhead = smallhead.next
            else:
                tmp = smallhead.next
                smallhead.next = bighead
                smallhead = bighead
                bighead = tmp
        smallhead.next = bighead
        return header
