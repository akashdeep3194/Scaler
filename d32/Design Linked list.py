# Definition for singly-linked list.
from typing import *


class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    # @param A : list of list of integers
    # @return the head node in the linked list

    def zero(self,head,value,leng):
        new_head_node = ListNode(value)
        new_head_node.next = head
        leng[0] = leng[0]+1        
        return new_head_node

    def one(self,head,value,leng):
        new_node = ListNode(value)
        if head is None:
            leng[0] = leng[0]+1        
            head = new_node
            return head
        iter_head = head
        while iter_head.next is not None:
            iter_head = iter_head.next

        iter_head.next = new_node
        leng[0] = leng[0]+1        
        return head

    def two(self,head,value,ind,leng):
        new_node = ListNode(value)

        ctr = 0

        iter_head = head
        
        if iter_head is None:
            leng[0] += 1
            return new_node
        if ctr==ind:
            new_node.next = iter_head
            leng[0] += 1            
            return new_node
            
        while iter_head.next is not None and ctr<ind-1:
            iter_head = iter_head.next
            ctr+=1
        
        if ctr == ind-1:
            tmp = iter_head.next
            iter_head.next = new_node
            new_node.next = tmp
            leng[0] = leng[0]+1
        
        return head

    def three(self,head,ind,leng):
        if head is None:
            return None
        if ind == 0:
            tmp = head.next
            del(head)                         
            leng[0] = leng[0]-1
            return tmp
        else:
            iter_head = head

            while ind>1 and iter_head.next.next is not None:
                iter_head = iter_head.next
                ind -= 1

            if ind == 1:
                tmp = iter_head.next
                iter_head.next = iter_head.next.next
                del(tmp)
                leng[0] = leng[0]-1

            return head

        
    def solve(self, A):
        head = None
        leng = [0]

        for ele in A:

            if ele[0] == 0:
                head = self.zero(head,ele[1],leng)
            elif ele[0] == 1:
                head = self.one(head,ele[1],leng)
            elif ele[0] == 2:
                if ele[2] == leng[0]:
                    head = self.one(head,ele[1],leng)
                elif ele[2]<leng[0]:
                    head = self.two(head,ele[1],ele[2],leng)
            elif ele[0] == 3:
                if ele[1]<=leng[0]-1:
                    head = self.three(head,ele[1],leng)
        return head

# A = [  [1, 13, -1],  [3, 0, -1]
# ,  [3, 1, -1]
# ,  [2, 15, 0]
# ,  [3, 0, -1]
# ,  [1, 12, -1]
# ,  [3, 0, -1]
# ,  [1, 19, -1]
# ,  [1, 13, -1]
# ,  [3, 0, -1]
# ,  [0, 12, -1]
# ,  [1, 13, -1]
# ,  [3, 2, -1]
# ]

# A = [  [2, 1, 0]
# ,  [3, 0, -1]
# ,  [0, 15, -1]
# ,  [3, 0, -1]
# ,  [0, 8, -1]
# ,  [2, 5, 0]
# ,  [1, 2, -1]
# ,  [3, 2, -1]
# ,  [3, 1, -1]
# ,  [3, 0, -1]
# ,  [0, 1, -1]
# ]

# s = Solution()

# final_head = s.solve(A)

# while final_head is not None:
#     print(final_head.val,end = "->")
#     final_head = final_head.next

