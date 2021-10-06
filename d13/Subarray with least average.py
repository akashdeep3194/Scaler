class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        s = 0
        ans = -1

        if B>len(A):
            return ans

        for i in range(B):
            s += A[i]
        ans = 0
        sm = s

        for i in range(1,len(A)-B+1):
            s = s - A[i-1] + A[i+B-1]
            if sm>s:
                ans = i
                sm = s
        return ans

s = Solution()
print(s.solve([ 5, 15, 7, 6, 3, 4, 18, 14, 13, 7, 3, 7, 2, 18 ],6))
