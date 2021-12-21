class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if A == 1:
            return 0
        sa = self.solve(A-1,(B+1)//2)
        
        if B%2 == 0:
            return (1+sa)%2
        else:
            return (0+sa)%2

if __name__ == '__main__':
    s = Solution()
    print(s.solve(3,2))
