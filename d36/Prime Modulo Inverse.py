class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer

    def pow(self, A, B, C):
        if A==0:
            return A
        if B==0:
            return 1
        if B==1:
            return A%C
        
        if B%2 == 0:
            sa = pow(A,B//2,C)
            ans = (sa*sa)%C
        else:
            sa = pow(A,B//2,C)
            ans = ((sa*sa)%C*(A%C))%C
        
        return ans

    def solve(self, A, B):
        return self.pow(A,B-2,B)

if __name__ == '__main__':
    s = Solution()
    print(s.solve( A = 3, B = 5))
