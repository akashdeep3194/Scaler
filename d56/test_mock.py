# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        head1 = A
        head2 = B
        i = 0
        carry = 0

        while head1 is not None and head2 is not None:
            digit = head1.val + head2.val + carry
            carry = digit//10
            digit = digit % 10
            new_node = ListNode(digit)
            if i == 0:
                head3 = new_node
                new_head = head3
                i += 1
            else:
                new_head.next = new_node
                new_head = new_node
            head1 = head1.next
            head2 = head2.next

        if head1 is None:
            head1 = head2

        while head1 is not None:
            digit = head1.val + carry
            carry = digit//10
            digit = digit % 10
            new_node = ListNode(digit)
            new_head.next = new_node
            new_head = new_node
            head1 = head1.next

        return head3
