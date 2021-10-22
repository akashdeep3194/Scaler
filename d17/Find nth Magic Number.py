from math import log
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        ans = 0
        k = A

        while(A>0):
            k = int(log(A,2))+1
            ans += 5**(k)
            A = A - 2**(k-1)

        return ans

# s = Solution()
# print(s.solve(10))
