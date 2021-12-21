class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        i = A[0]
        for ele in A:
            if ele != i:
                return 0
            i += 1
        return 1

if __name__ == '__main__':
    A = [ 1, 2, 3, 4, 5 ]
    s = Solution()
    print(s.solve(A))
