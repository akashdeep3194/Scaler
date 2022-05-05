class Solution:
    # @param A : list of list of integers
    # @return an integer
    def __init__(self) -> None:
        self.ans = self.area = 0

    def maxArea(self, arr, i):
        left_nearest_smaller = []
        right_nearest_smaller = [len(arr[0])]*len(arr[0])

        s = [(-1, -1)]
        t = [(-1, len((arr[0])))]
        for j, ele in enumerate(arr[i]):
            if s[-1][0] < ele:
                left_nearest_smaller.append(s[-1][1])
                s.append((ele, j))
            else:
                while s[-1][0] >= ele:
                    s.pop()
                left_nearest_smaller.append(s[-1][1])
                s.append((ele, j))

        for j in range(len(arr[i])-1, -1, -1):
            ele = arr[i][j]
            if t[-1][0] < ele:
                right_nearest_smaller[j] = (t[-1][1])
                t.append((ele, j))
            else:
                while t[-1][0] >= ele:
                    t.pop()
                right_nearest_smaller[j] = (t[-1][1])
                t.append((ele, j))
        max_area = 0
        for ind, ele in enumerate(arr[i]):
            area = ele * \
                (right_nearest_smaller[ind] - left_nearest_smaller[ind] - 1)
            max_area = max(area, max_area)
        return max_area

    def maximalRectangle(self, A):
        dp = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
        for i, ele in enumerate(A[-1]):
            dp[-1][i] = ele
        for i in range(len(A)-2, -1, -1):
            for j in range(len(A[0])):
                if A[i][j] == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i+1][j] + A[i][j]
        for i in range(len(dp)):
            self.area = self.maxArea(dp, i)
            self.ans = max(self.area, self.ans)
        return self.ans


if __name__ == '__main__':
    A = [
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    ]

    s = Solution()
    print(s.maximalRectangle(A))
