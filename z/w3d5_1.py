import sys


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve_helper(self, A):
        sec_max = maxn = A[0]
        for ind,ele in enumerate(A):
            if ele >= maxn:
                sec_max = maxn
                maxn = ele
            elif ele > sec_max:
                sec_max = ele
            elif sec_max == maxn and ind == 1:
                sec_max = ele
        return maxn, sec_max

    def solve(self, A):
        ret_arr = []
        m, s = self.solve_helper(A)
        print(m,s)
        for ele in A:
            if ele == m or ele == s:
                continue
            else:
                ret_arr.append(ele)
        return ret_arr


s = Solution()
arr = list(map(int, sys.stdin.readline().strip().split()))
print(s.solve(arr))
