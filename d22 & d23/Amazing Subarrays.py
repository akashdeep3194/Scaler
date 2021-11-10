
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)
        ans = 0
        for i, ele in enumerate(A):
            if ele in ('a','e','i','o','u','A','E','I','O','U'):
                ans += (n-i)
                ans = ans%10003
        return ans

# s = Solution()
# print(s.solve("aBEiouCA"))
