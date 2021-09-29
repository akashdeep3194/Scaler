class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        ans = [[] for _ in range(len(B))]
        reva = A[::-1]
        for ind,ele in enumerate(B):
            ele = ele%len(A)
            ele = len(A)-ele
            r = reva[:ele][::-1]
            r.extend(reva[ele:][::-1])
            ans[ind] = r[:]
        return ans
            
# s = Solution()
# print(s.solve([1,2,3,4,5],[2,3]))