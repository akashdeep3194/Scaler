class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        if A[0] > A[1]:
            return A[0]
        if A[-1] > A[-2]:
            return A[-1]

        start = 1
        end = len(A)-2

        while start <= end:
            mid = start + (end-start+1)//2
            if A[mid+1] < A[mid] > A[mid-1]:
                return A[mid]
            elif A[mid+1] > A[mid]:
                start = mid+1
            elif A[mid+1] < A[mid]:
                end = mid-1


if __name__ == '__main__':
    s = Solution()
    print(s.solve([5, 17, 100, 11]))
