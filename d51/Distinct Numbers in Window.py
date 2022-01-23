class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        dc = dict()
        ans = []
        i = 0
        j = B - 1
        for i in range(i, j+1):
            dc[A[i]] = dc.get(A[i], 0) + 1
        ans.append(len(dc.keys()))

        for i in range(1, len(A)-B+1):
            dc[A[i-1]] -= 1
            if dc[A[i-1]] == 0:
                dc.pop(A[i-1])
            dc[A[i+B-1]] = dc.get(A[i+B-1], 0) + 1
            ans.append(len(dc.keys()))
        return ans


if __name__ == "__main__":
    s = Solution()
    A = [1, 2, 1, 3, 4, 3]
    B = 3
    print(s.dNums(A, B))
