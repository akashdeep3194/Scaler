class Solution:
    # @param A : list of integers
    # @return a list of integers

    def solve(self, A):
        ans = 0
        a = A
        k = 31
        while a > 0:
            j = a & 1
            ans += (2 ** k) * j
            a = a >> 1
            k -= 1
        return ans


s = Solution()
print(s.solve(3))

