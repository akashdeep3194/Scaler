class Solution:
    # @param A : list of integers
    # @return an integer
    def gcd(self,A,B):
        if A>B:
            A,B = B,A

        while A > 0:

            B = B%A

            if A>B:
                A,B = B,A

        return B

    def solve(self, A):
        gcdl = 0
        
        for i in range(0,len(A)):
            gcdl = self.gcd(gcdl,A[i])
        return gcdl

if __name__ == '__main__':
    A = [ 3, 9, 6, 8, 3 ]
    s = Solution()
    print(s.solve(A))
