class Solution:
    # @param A : list of integers
    # @return a list of integers

    def countTotalSetBits(self, x: int) -> int:
        ctr = 0

        while x > 0:
            if x & 1 == 1:
                ctr += 1
            x = x >> 1
        return ctr

    def solve(self, A, B):
        a = A
        b = B

        total_bits = self.countTotalSetBits(a)

        if b > total_bits:
            b = b - total_bits
            a = ~a
            while b > 0:
                a = a & a - 1
                b-=1
            a = ~a
        else:
            b = total_bits - b
            while b > 0:
                a = a & a - 1  # right most non zero bit is converted to zero
                b-=1
        return a

s = Solution()
print(s.solve(3, 3))
