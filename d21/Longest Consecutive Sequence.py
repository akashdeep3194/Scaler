class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        hs = set()
        for ele in A:
            hs.add(ele)

        f_ans = 1

        for ele in hs:
            ans = 1
            if (ele-1) in hs:
                continue
            else:
                ele += 1
                while ele in hs:
                    ele += 1
                    ans += 1
                f_ans = max(ans,f_ans)
        return f_ans

# s = Solution()
# A = [100, 4, 200, 1, 3, 2]
# print(s.longestConsecutive(A))
