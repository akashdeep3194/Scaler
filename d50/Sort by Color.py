class Solution:
    # @param A : list of integers
    # @return a list of integers
    def sortColors(self, A):
        fnz = lnt = -1
        for index, ele in enumerate(A):
            if ele != 0:
                fnz = index
                break
        for i in range(len(A)-1, -1, -1):
            if A[i] != 2:
                lnt = i
                break
        i = fnz
        while i < len(A):
            if A[i] == 2 and lnt > i:
                A[i], A[lnt] = A[lnt], A[i]
                lnt -= 1
                while lnt > fnz and A[lnt] == 2:
                    lnt -= 1
            elif A[i] == 0 and fnz < i:
                A[i], A[fnz] = A[fnz], A[i]
                fnz += 1
                while fnz < lnt and A[fnz] == 0:
                    fnz += 1
            else:
                i += 1
        return A


if __name__ == "__main__":
    s = Solution()
    A = [2, 1, 2]
    # , 1, 1, 2, 1, 2, 0, 0, 2, 1, 0, 1]
    print(s.sortColors(A))
