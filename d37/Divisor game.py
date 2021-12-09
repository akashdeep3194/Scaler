class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer

    def gcd(self, A, B):
        if A>B:
            A,B = B,A

        while A > 0:

            B = B%A
            if A>B:
                A,B = B,A
        return B

    def solve(self, A, B, C):
        sa = B*C
        ans = 0

        i = 2
        isa = B*C//self.gcd(B,C)
        sa = isa

        while sa<=A:
            ans+=1
            sa *= i
            i+=1
            if sa>A:
                break
            sa = isa

        return ans

if __name__ == '__main__':
    A = 81991
    B = 2549
    C = 7

    s = Solution()
    print(s.solve(A,B,C))
