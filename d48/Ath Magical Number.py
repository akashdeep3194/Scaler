class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def gcd(self, A, B):
        a = A
        b = B
        A = max(a, b)
        B = min(a, b)
        while B != 0:
            A = A % B
            if A < B:
                A, B = B, A
        return A

    def solve(self, A, B, C):
        Z = 10**9+7
        gcd_val = self.gcd(B, C)
        lcm = int(B*C/(gcd_val))
        start = min(B, C)
        end = min(B, C)*A
        while start <= end:
            mid = (start+end)//2
            n = int(mid//B + mid//C - mid//lcm)
            if n == A:
                if mid % B == 0 or mid % C == 0:
                    return mid % Z
                else:
                    k = min(mid % B, mid % C)
                    return (mid-k) % Z
            elif n > A:
                end = mid - 1
            else:
                start = mid + 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.solve(11, 12, 13))
