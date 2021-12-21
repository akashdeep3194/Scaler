class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A == 0:
            return 0
        rem = A%10
        A = A//10
        sa = self.solve(A)
        ans = sa + rem
        
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.solve(23))
