class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        hs = set()
        ans = 0
        for ele in A:
            find = ele^B
            if find in hs:
                ans += 1
            hs.add(ele)
        return ans

# s = Solution()
# A = [5, 4, 10, 15, 7, 6]
# B = 5
# print(s.solve(A,B))
