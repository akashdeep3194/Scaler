class Solution:
    # @param A : tuple of integers
    # @return an integer
    def checkLongest(self, s, ele):
        l = 1
        ele += 1
        while ele in s:
            l += 1
            ele += 1
        return l

    def longestConsecutive(self, A):
        dc = set()
        ans = 1
        l = 1
        for ele in A:
            dc.add(ele)
        for i in range(len(A)):
            if A[i]-1 in dc:
                continue
            else:
                l = self.checkLongest(dc, A[i])
            ans = max(ans, l)
        return ans


if __name__ == "__main__":
    s = Solution()
    A = [100, 4, 200, 1, 3, 2]
    print(s.longestConsecutive(A))
