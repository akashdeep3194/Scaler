class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        A = sorted(A)
        magicmn = magicmx = 0
        i = 0
        j = 0
        while i < len(A)-1:
            magicmn = (magicmn + abs(A[i]-A[i+1])) % (10**9+7)
            magicmx = (magicmx + abs(A[j]-A[len(A)-1-j])) % (10**9+7)
            i += 2
            j += 1
        return [magicmx, magicmn]


if __name__ == '__main__':
    s = Solution()
    print(s.solve([3, 11, -1, 5]))
