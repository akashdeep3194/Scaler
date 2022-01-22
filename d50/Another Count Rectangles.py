class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        z = 10**9+7
        i = 0
        j = len(A)-1
        ctr = 0
        while i <= j:
            if i == j:
                if A[i]*A[j] >= B:
                    ctr = (ctr + j) % z
                else:
                    ctr = (ctr + j + 1) % z
                return ctr % z
            if A[i]*A[j] < B:
                ctr += ((j-i)*2) % z
                i += 1
            elif A[i]*A[j] >= B:
                j -= 1
        return ctr % z


if __name__ == '__main__':
    s = Solution()
    A = [4, 14, 23, 25, 32, 45]
    B = 81
    print(s.solve(A, B))
