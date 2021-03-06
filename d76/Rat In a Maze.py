class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def recfn(self, A, i, j, path):
        if i == len(A)-1 and j == len(A[0])-1:
            A[i][j] = 2
            path[i][j] = 1
            return True
        if i < 0 or j < 0 or i > len(A)-1 or j > len(A[0])-1:
            return False
        if A[i][j] == 0 or A[i][j] == 2:
            return False
        path[i][j] = 1

        A[i][j] = 2

        # up
        if self.recfn(A, i-1, j, path):
            return True
        # down
        if self.recfn(A, i+1, j, path):
            return True
        # left
        if self.recfn(A, i, j-1, path):
            return True
        # right
        if self.recfn(A, i, j+1, path):
            return True

        A[i][j] = 1
        path[i][j] = 0

    def solve(self, A):
        path = [[0 for _ in range(len(A[0]))]for _ in range(len(A))]
        self.recfn(A, 0, 0, path)
        return path


if __name__ == '__main__':
    A = [[1, 0], [1, 1]]
    s = Solution()
    print(s.solve(A))
