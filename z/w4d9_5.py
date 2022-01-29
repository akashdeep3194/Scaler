class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        a = A
        l = len(a)
        arr = []
        for i in range(l-1):
            arr.append(a[i+1]-a[i])
        return arr

# s = Solution()
# a = [2]
# print(s.solve(a))
