class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        i = 0
        # for i in range(len(A)):
        r = -1

        if A[0][0] > B or A[-1][-1] < B:
            return 0
        if A[0][0] == B:
            return 1
        if A[-1][-1] == B:
            return 1
        if A[-1][0] <= B:
            r = len(A)-1

        si = 0
        ei = len(A)-1

        if r == -1:
            while si <= ei:
                mid = si + (ei - si + 1)//2
                if A[mid][0] == B:
                    return 1
                if A[mid][0] <= B and A[mid+1][0] > B:
                    r = mid
                    break
                elif A[mid][0] <= B:
                    si = mid + 1
                else:
                    ei = mid - 1

        start = 0
        end = len(A[0]) - 1

        while start <= end:
            mid = start + (end-start + 1)//2
            if A[r][mid] == B:
                return 1
            elif A[r][mid] > B:
                end = mid - 1
            else:
                start = mid + 1
        return 0


if __name__ == '__main__':
    s = Solution()
    # A = [
    #     [1,   3,  5,  7],
    #     [10, 11, 16, 20],
    #     [23, 30, 34, 50],
    # ]
    # A = [
    #     [5, 17, 100, 111],
    #     [119, 120, 127, 131],
    # ]
    # B = 3
    A = [
        [20, 21, 44, 48, 62, 64, 65, 73, 77]
    ]
    B = 59

    print(s.searchMatrix(A, B))
