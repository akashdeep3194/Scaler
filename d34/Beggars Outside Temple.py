from typing import AnyStr


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        ans = [0 for _ in range(A)]
        for ele in B:
            s = ele[0] - 1
            e = ele[1] - 1
            amt = ele[2]
            ans[s] += amt
            if e+1<A:
                ans[e+1] -= amt
        for i,ele in enumerate(ans[1:]):
            ans[i+1] += ans[i]

        return ans
    
# s = Solution()
# print(s.solve(5,[[1, 2, 10], [2, 3, 20], [2, 5, 25]]))
