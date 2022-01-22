class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def maxBooksLteMid(self, A, B, mid):
        count = 1
        mxBooks = 0
        for i in range(len(A)):
            if mxBooks+A[i] > mid:
                count += 1
                if count > B:
                    return False
                mxBooks = A[i]
            else:
                mxBooks += A[i]

        return True

    def books(self, A, B):
        if B > len(A):
            return -1
        ans = -1
        sm = 0
        start = max(A)
        for i in range(len(A)):
            sm += A[i]
        stop = sm

        while start <= stop:
            mid = (start+stop)//2
            if self.maxBooksLteMid(A, B, mid):
                ans = mid
                stop = mid - 1
            else:
                start = mid + 1
        return ans


if __name__ == '__main__':
    s = Solution()
    A = [31, 14, 19, 75]
    B = 12
    print(s.books(A, B))
