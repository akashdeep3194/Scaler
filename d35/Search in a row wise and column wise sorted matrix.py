import sys

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer

    def solve(self, A, B):
        n = len(A)
        m = len(A[0])

        ans = sys.maxsize

        i = 0
        j = m-1
        af = 0

        while i<n and j>=0:
            if A[i][j] == B:
                ans = min(ans,(i+1)*1009+j+1)
                af = 1
                j -= 1

            elif B<A[i][j]:
                j -= 1
            else:
                i += 1

        if af == 0:
            return -1
        else:
            return ans

if __name__ == '__main__':
    A = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
    B = 2

    s = Solution()
    print(s.solve(A,B))
