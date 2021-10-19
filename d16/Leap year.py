class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A%100 == 0:
            if A%400 == 0:
                return 1
            else:
                return 0
        if A%4 == 0:
            return 1
        else:
            return 0
# s = Solution()
# print(s.solve(1999))
