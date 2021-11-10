class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        j=0
        min_len = len(A[0])
        for ele in A:
            min_len = min(len(ele),min_len)

        while j<min_len:
            e = A[0][j]

            for ele in A:
                if e != ele[j]:
                    return ele[:j]
            j += 1
        return A[0][:j]

# s = Solution()
# print(s.longestCommonPrefix(["pskabc","pskab","pskxy","pskzz"]))
