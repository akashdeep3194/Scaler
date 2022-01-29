class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        dcxy = dict()
        ctr = 0

        for i in range(len(A)):
            dcxy[(A[i], B[i],)] = 1

        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if A[i] == A[j] or B[i] == B[j]:
                    continue
                if dcxy.get((A[j], B[i]), 0) != 0 and dcxy.get((A[i], B[j]), 0) != 0:

                    ctr += 1

        return ctr//2


if __name__ == "__main__":
    s = Solution()
    A = [1, 1, 2, 2, 3, 3]
    B = [1, 2, 1, 2, 1, 2]
    print(s.solve(A, B))
