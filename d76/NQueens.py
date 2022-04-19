import copy


class Solution:
    # @param A : integer
    # @return a list of list of strings
    def __init__(self) -> None:
        self.answer = []

    def canBePlaced(self, board, i, j):
        if "Q" in board[i]:
            return False
        for k in range(len(board)):
            if board[k][j] == "Q":
                return False
        m = i
        n = j
        while m >= 0 and n >= 0:
            if board[m][n] == "Q":
                return False
            m -= 1
            n -= 1

        m = i
        n = j
        while m < len(board) and n < len(board):
            if board[m][n] == "Q":
                return False
            m += 1
            n += 1

        m = i
        n = j
        while m < len(board) and n >= 0:
            if board[m][n] == "Q":
                return False
            m += 1
            n -= 1

        m = i
        n = j
        while m >= 0 and n < len(board):
            if board[m][n] == "Q":
                return False
            m -= 1
            n += 1

        return True

    def recfn(self, board, x):
        if x == len(board):
            self.answer.append(copy.deepcopy(board))
            return True

        m = x
        for n in range(len(board[0])):
            if self.canBePlaced(board, m, n):
                board[m][n] = "Q"
                self.recfn(board, x+1)
                board[m][n] = "."
            else:
                continue

    def solveNQueens(self, A):
        board = [["." for ele in range(A)] for ele in range(A)]
        self.recfn(board, 0)
        for ele in self.answer:
            for i, char in enumerate(ele):
                ele[i] = "".join(char)
        return self.answer


if __name__ == '__main__':
    A = 4
    s = Solution()
    print(s.solveNQueens(A))
