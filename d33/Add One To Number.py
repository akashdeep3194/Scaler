class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        carry = 1
        first_zero = -1
        for i in range(len(A)-1,-1,-1):
            if first_zero == -1 and A[i] == 0:
                first_zero = i
            elif first_zero != -1 and A[i] != 0:
                first_zero = -1
            digit = A[i] + carry
            carry = digit//10
            digit = digit%10
            A[i] = digit

        if carry == 1:
            li = [1]
            li.extend(A)
            return li
        elif first_zero != -1:
            if A[first_zero] == 0:
                return A[first_zero+1:]
            else:
                return A[first_zero:] 
        return A[:]
 
# s = Solution()
# print(s.plusOne([0,0,1,0,0,0,0,1,9,9,5]))
