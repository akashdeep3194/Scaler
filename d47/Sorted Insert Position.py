class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        start = 0
        end = len(A)-1
        if A[0] > B:
            return 0
        if A[-1] < B:
            return len(A)

        while start <= end:
            mid = start + (end - start + 1)//2
            if mid > 0 and A[mid-1] < B and A[mid] > B:
                return mid
            if A[mid] == B:
                return mid
            elif A[mid] > B:
                end = mid - 1
            elif A[mid] < B:
                start = mid + 1
