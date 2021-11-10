class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        A = list(A)
        for i, ele in enumerate(A):
            ele = list(ele)
            A[i] = ele
        for r in range(len(A)):
            hmr = dict()
            hmc = dict()
            hmb = dict()
            for c in range(len(A[0])):
                if A[r][c] == ".":
                    pass
                else:
                    hmr[A[r][c]] = hmr.get(A[r][c],0) + 1
                    if hmr[A[r][c]] > 1:
                        return 0
                if A[c][r] == ".":
                    pass
                else:
                    hmc[A[c][r]] = hmc.get(A[c][r],0) + 1
                    if hmc[A[c][r]] > 1:
                        return 0
                if A[3*(r//3)+c//3][3*(r%3)+c%3] == ".":
                    # print(3*(r//3)+c//3,3*(r%3)+c%3, end=" ",sep="")
                    pass

                else:
                    hmb[A[3*(r//3)+c//3][3*(r%3)+c%3]] = hmb.get(A[3*(r//3)+c//3][3*(r%3)+c%3],0) + 1
                    # print(3*(r//3)+c//3,3*(r%3)+c%3,end=" ",sep="")
                    if hmb[A[3*(r//3)+c//3][3*(r%3)+c%3]] > 1:
                        return 0
            # print()
        return 1


s = Solution()
A = [ "....5..1.", ".4.3.....", ".....3..1", "8......2.", "..2.7....", ".15......", ".....2...", ".2.9.....", "..4......" ]
print(s.isValidSudoku(A))
