class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def minindexBinarySearch(self, A, B):
        start = 0
        end = len(A)-1
        min_ind = end
        if A[start] == B:
            return start

        while start <= end:
            mid = start + (end - start + 1)//2
            if A[mid] == B and A[mid-1] != B:
                return mid
            elif A[mid] >= B:
                end = mid - 1
            elif A[mid] < B:
                start = mid + 1

    def searchRange(self, A, B):
        ans = [-1, -1]
        start = 0
        end = len(A) - 1
        ind = -1

        while start <= end:
            mid = start + (end - start + 1)//2
            if A[mid] == B:
                ind = mid
            elif A[mid] < B:
                start = mid + 1
            else:
                end = mid - 1

        if ind == -1:
            return ans
        else:
            si = ei = ind

        if A[start] == B:
            si = start

        while ind != 0 and A[ind - 1] == B:
            ind = (start + ind)//2

        if A[end] == B:
            ei = end

        ans = [si, ei]

        return ans


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def minIndexBinarySearch(self, A, B, si, ei):
        start = si
        end = ei
        if A[start] == B:
            return start

        while start <= end:
            mid = start + (end - start + 1)//2
            if A[mid] == B and A[mid-1] != B:
                return mid
            elif A[mid] >= B:
                end = mid - 1
            elif A[mid] < B:
                start = mid + 1

    def maxIndexBinarySearch(self, A, B, si, ei):
        start = si
        end = ei
        if A[end] == B:
            return end

        while start <= end:
            mid = start + (end - start + 1)//2
            if A[mid] == B and A[mid+1] != B:
                return mid
            elif A[mid] > B:
                end = mid - 1
            elif A[mid] <= B:
                start = mid + 1

    def searchRange(self, A, B):
        ans = [-1, -1]
        start = 0
        end = len(A) - 1
        ind = -1

        while start <= end:
            mid = start + (end - start + 1)//2
            if A[mid] == B:
                ind = mid
                break
            elif A[mid] < B:
                start = mid + 1
            else:
                end = mid - 1

        if ind == -1:
            return ans

        si = self.minIndexBinarySearch(A, B, 0, ind)
        ei = self.maxIndexBinarySearch(A, B, ind, len(A)-1)

        ans = [si, ei]
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([1, 1, 2, 3, 3, 4, 4, 4, 5,
                         6, 6, 6, 6, 6, 6, 6, 7, 8, 8, 9, 9, 9], 6))
