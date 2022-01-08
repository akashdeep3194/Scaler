from typing import List


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def maxSumSubArrSizeK(self, arr, k, limit):
        sm = 0
        for i in range(k):
            sm += arr[i]
        ans = sm
        i = 1
        j = k
        while j < len(arr):
            if sm > limit:
                return sm
            sm = sm + arr[j] - arr[i-1]
            ans = max(ans, sm)
            j += 1
            i += 1
        return ans

    def solve(self, A: List, B):
        ans = 0
        start = 1
        end = len(A)
        while start <= end:
            k = (start+end)//2
            pa = self.maxSumSubArrSizeK(A, k, B)
            if pa == B:
                ans = k
                return ans
            if pa < B:
                start = k + 1
                ans = max(ans, k)
            elif pa > B:
                end = k - 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.solve(A=[5, 17, 100, 11], B=130))
