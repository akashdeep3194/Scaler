from queue import Queue


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        if B == C:
            return 1
        if A[B-1] == C:
            return 1
        x = A[B-1]

        while x-1 > 0:
            if A[x-1] == C:
                return 1
            x = A[x-1]

        return 0


if __name__ == '__main__':
    A = [1, 1, 1, 3, 3, 2, 2, 7, 6]
    B = 9
    C = 1
    s = Solution()
    print(s.solve(A, B, C))
