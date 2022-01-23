class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        dc = dict()
        ans = len(A)
        for i in range(len(A)):
            arr = dc.get(A[i], [])
            arr.append(i)
            dc[A[i]] = arr
            if len(arr) >= 2:
                ans = min(arr[-1]-arr[-2], ans)
        if ans == len(A):
            return -1
        return ans


if __name__ == '__main__':
    s = Solution()
    A = [1, 2, 3, 2, 5, 6, 4, 5, 6, 3, 2, 2]
    print(s.solve(A))
