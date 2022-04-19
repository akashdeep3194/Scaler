class Solution:
    # @param A : list of list of chars

    def inCell(self, board, num, cell):
        sc = (cell % 3)*3
        sr = (cell//3)*3
        for i in range(sr, sr+3):
            for j in range(sc, sc+3):
                if num == board[i][j]:
                    return True
        return False

    def canBePlaced(self, board, i, j, num):
        if num in board[i]:
            return False

        for k in range(len(board)):
            if board[k][j] == num:
                return False

        cell = 3*(i//3)+j//3
        if self.inCell(board, num, cell):
            return False

        return True

    def recfn(self, board, x):

        for i in range(x, 9):
            for j in range(9):
                if board[i][j] == ".":
                    for k in range(1, 10):
                        if self.canBePlaced(board, i, j, str(k)):
                            board[i][j] = str(k)
                            if self.recfn(board, i):
                                return True
                            board[i][j] = "."
                        else:
                            continue
                    else:
                        return False
                else:
                    continue
        return True

    def solveSudoku(self, A):
        self.recfn(A, 0)
        return A


if __name__ == '__main__':
    A = [["53..7...."], ["6..195..."], [".98....6."], ["8...6...3"], [
        "4..8.3..1"], ["7...2...6"], [".6....28."], ["...419..5"], ["....8..79"]]
    for ind, arr in enumerate(A):
        li = []
        for i, ele in enumerate(arr[0]):
            li.append(ele)
        A[ind] = li.copy()
    s = Solution()
    for ele in s.solveSudoku(A):
        print(ele)
