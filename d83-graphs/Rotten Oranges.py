from queue import Queue


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):

        q = Queue()

        ans = [[2**31 for _ in range(len(A[0]))] for _ in range(len(A))]

        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 2:
                    q.put([i, j])
                    ans[i][j] = 0

        while not q.empty():
            x = q.get()
            val = A[x[0]][x[1]]

            if x[1] + 1 < len(A[0]) and A[x[0]][x[1]+1] == 1:
                ans[x[0]][x[1]+1] = ans[x[0]][x[1]] + 1
                A[x[0]][x[1]+1] = 2
                q.put([x[0], x[1]+1])

            if x[0] - 1 >= 0 and A[x[0]-1][x[1]] == 1:
                ans[x[0]-1][x[1]] = ans[x[0]][x[1]] + 1
                A[x[0]-1][x[1]] = 2
                q.put([x[0]-1, x[1]])

            if x[1] - 1 >= 0 and A[x[0]][x[1]-1] == 1:
                ans[x[0]][x[1]-1] = ans[x[0]][x[1]] + 1
                A[x[0]][x[1]-1] = 2
                q.put([x[0], x[1]-1])

            if x[0] + 1 < len(A) and A[x[0]+1][x[1]] == 1:
                ans[x[0]+1][x[1]] = ans[x[0]][x[1]] + 1
                A[x[0]+1][x[1]] = 2
                q.put([x[0]+1, x[1]])

        answer = -1

        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    return -1
                if A[i][j] == 0:
                    continue
                else:
                    answer = max(answer, ans[i][j])

        return answer


if __name__ == '__main__':
    A = [[2, 1, 1],
         [1, 1, 0],
         [0, 1, 1], ]
    s = Solution()
    print(s.solve(A))
