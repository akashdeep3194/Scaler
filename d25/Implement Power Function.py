import sys
sys.setrecursionlimit(10**5)

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):
        if B == 0:
            return 1%C
        if 0<=A <= 1 or B == 1:
            return A%C
        else:
            if B&1 == 1:
                B -= 1
                sa = self.pow(A,B//2,C)
                ans = (((sa*sa)%C)*A)%C
            else:
                sa = self.pow(A,B//2,C)
                ans = sa*sa%C
        return ans

# s = Solution()
# print(s.pow(-1,2,20))
