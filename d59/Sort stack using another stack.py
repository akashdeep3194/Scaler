class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        B = []
        x = A.pop()
        B.append(x)
        while len(A) > 0:
            x = A.pop()
            if x >= B[-1]:
                B.append(x)
            else:
                while len(B) > 0 and x < B[-1]:
                    A.append(B.pop())
                B.append(x)
        return B


if __name__ == "__main__":
    s = Solution()
    A = [10, 5, 4, 2, 1, 3, 6, 8, 9, 7]
    print(s.solve(A))
