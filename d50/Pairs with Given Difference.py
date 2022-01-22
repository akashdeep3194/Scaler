class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A.sort()
        i = 0
        j = 1
        count = 0
        ans = set()
        while i < len(A) and j < len(A):

            if A[j]-A[i] == B:
                if i != j:
                    count += 1
                    ans.add((A[j], A[i]))
                    i += 1
                else:
                    j += 1
            elif A[j]-A[i] > B:
                i += 1
            elif A[j]-A[i] < B:
                j += 1
        return len(ans)


if __name__ == "__main__":
    s = Solution()
    A = [1, 8, 2, 8, 8, 8, 8, 4, 4, 6, 10, 10, 9, 2, 9, 3, 7]
    B = 1
    print(s.solve(A, B))
