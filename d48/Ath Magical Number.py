class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        Z = (10**9+7)
        b = B
        c = C
        B = max(c, b)
        C = min(c, b)
        if B == 1:
            return A
        m = B % C
        if m == 1:
            m = B//C
        if (A) % (m+1) == 0:
            return ((B % Z)*(A//(m+1)) % Z) % Z
        else:
            return ((C % Z)*(A-(A//(m+1)) % Z) % Z)


if __name__ == '__main__':
    s = Solution()
    print(s.solve(6, 6, 9))
