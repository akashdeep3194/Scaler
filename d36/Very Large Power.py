import sys
sys.setrecursionlimit(10**4)

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    
    def powmod(self,A,B,C):

        if A == 0:
            return 0
        if B == 0:
            return 1
        if B == 1:
            return A%C
        if B%2 == 0:
            sa = self.powmod(A,B//2,C)
            return (sa*sa)%C
        else:
            sa = self.powmod(A,B//2,C)
            return ((sa*sa)%C*A%C)%C
                    
    def factmod(self, B, C):
        if B == 1 or B == 0:
            return 1

        ans = 1

        while B>1:
            ans = (B%C*ans)%C
            B-=1    

        return ans

    def solve(self, A, B):
        C = 10**9+7
        sa = self.factmod(B,C-1)
        ans = self.powmod(A,sa,C)
        return ans

A = 135318
B = 197971

if __name__ == '__main__':
    s = Solution()
    print(s.solve(A,B))
