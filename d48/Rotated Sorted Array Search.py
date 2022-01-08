class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        ele = A[0]

        if A[0] == B:
            return 0
        if A[-1] == B:
            return len(A) - 1

        start = 0
        end = len(A)-1

        while start <= end:
            mid = start + (end - start + 1)//2
            if A[mid] == B:
                return mid
            if A[mid] < ele:
                if (A[mid] < B and B > ele) or (A[mid] > B):
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if A[mid] > B and B > ele:
                    end = mid - 1
                else:
                    start = mid + 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.search(A=[4, 5, 6, 7, 0, 1, 2, 3], B=1))
