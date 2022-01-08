class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        if len(A) == 1:
            return A[0]
        start = 1
        end = len(A)-2
        if A[0] != A[1]:
            return A[0]
        if A[-1] != A[-2]:
            return A[-1]
        while start <= end:
            mid = start + (end - start + 1)//2
            if A[mid] != A[mid-1] and A[mid] != A[mid+1]:
                return A[mid]
            elif A[mid] == A[mid + 1]:
                if mid % 2 == 0:
                    start = mid + 2
                else:
                    end = mid - 1
            elif A[mid] == A[mid - 1]:
                if mid % 2 == 0:
                    end = mid - 2
                else:
                    start = mid + 1
        return -1
