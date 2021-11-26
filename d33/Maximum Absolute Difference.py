class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        if len(A) == 0:
            return 0
        val1max = val1min = val2max = val2min = A[0]
        for i, ele in enumerate(A):
            val1max = max((A[i]+i),val1max)
            val1min = min((A[i]+i),val1min)

            val2max = max((A[i]-i),val2max)
            val2min = min((A[i]-i),val2min)

        ans1 = val1max - val1min
        ans2 = val2max - val2min

        return max(ans1,ans2)
