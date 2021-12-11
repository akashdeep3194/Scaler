import sys
sys.setrecursionlimit(10**6)

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def factmod(self,A,C,r):

        if A == 0 or A == 1:
            return 1,1
        ans = 1
        ans_2 = 1

        
        for i in range(A-r):
            ans = (A*ans)%C
            ans_2 = (ans_2*(i+1))%C            
            A -= 1

        return ans,ans_2

    def powmod(self,A,B,C):

        if A == 0:    
            return 0
        if B == 0 or A == 1:
            return 1

        res = 1

        while B>0:
            if B&1 != 0:
                res = (res*A)%C
            B = B//2
            A = (A*A)%C
        return res        
        
    def solve(self, A, B, C):
        B = max(B,A-B)
        n,n_r = self.factmod(A,C,B)
        a = self.powmod(n_r,C-2,C)
        
        return ((n*a)%C)

if __name__ == '__main__':
    s = Solution()
    print(s.solve(6,2,13))
