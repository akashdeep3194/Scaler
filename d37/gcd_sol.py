class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    
    def gcd(self, A, B):
        if A>B:
            A,B = B,A

        while A > 0:

            B = B%A
            if A>B:
                A,B = B,A
        return B

if __name__ == '__main__':
    s = Solution()
    print(s.gcd(500,150))
