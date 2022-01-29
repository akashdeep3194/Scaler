class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        maxn = minn = A[0]
        for ele in A:
            if ele>maxn:
                maxn = ele
            elif ele<minn:
                minn = ele
        minn = min(A)
        maxn = max(A)
        cnt = 0
        for ele in A:
            if ele != minn and ele != maxn:
                cnt += 1
        return cnt


s = Solution()
print(s.solve([1, 2, 3]))
