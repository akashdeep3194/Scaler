class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        x = list(zip(B, A))
        x.sort()
        ctr = 0
        free_at = 0
        for task in x:
            if task[1] >= free_at:
                ctr += 1
                free_at = task[0]
        return ctr


# s = Solution()
# A = [3, 7, 12, 4, 10, 8]
# B = [10, 16, 17, 8, 13, 9]
# print(s.solve(A, B))
