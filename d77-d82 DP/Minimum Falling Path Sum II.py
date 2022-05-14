class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minArr(self, A):
        min = sec_min = 2**32-1
        for ele in A:
            if ele < min:
                sec_min = min
                min = ele
            elif ele >= min and ele < sec_min:
                sec_min = ele
        ans = []
        for ele in A:
            if min == ele:
                ans.append(sec_min)
            else:
                ans.append(min)
        return ans

    def solve(self, A):
        dp = [
            [
                0 for ele in range(len(A[0]))
            ] for ele in range(len(A))
        ]
        for i, ele in enumerate(A[-1]):
            dp[-1][i] = ele

        for i in range(len(A)-2, -1, -1):
            min_arr = self.minArr(dp[i+1])
            for j in range(len(A[0])):
                dp[i][j] = A[i][j] + min_arr[j]

        ans = dp[0][0]
        for j in range(len(A[0])):
            ans = min(ans, dp[0][j])
        return ans


if __name__ == '__main__':
    A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    s = Solution()
    print(s.solve(A))
