class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        max = A[0]

        count = 0

        for ele in A:
            if ele>max:
                max = ele

        for ele in A:
            count+=max - ele
        return count
