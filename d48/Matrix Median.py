class Solution:
    # @param A : list of list of integers
    # @return an integer
    def count_greater_k(self, A, k):
        start = 0
        end = len(A)-1
        if A[-1] < k:
            return 0
        if A[0] >= k:
            return len(A)

        while start <= end:
            mid = (start+end)//2
            if A[mid] >= k and A[mid-1] < k:
                return len(A) - mid
            elif A[mid] >= k:
                end = mid - 1
            elif A[mid] < k:
                start = mid + 1

    def count_smaller_k(self, A, k):
        start = 0
        end = len(A)-1
        if A[-1] <= k:
            return len(A)
        if A[0] > k:
            return 0

        while start <= end:
            mid = (start+end)//2
            if A[mid] <= k and A[mid+1] > k:
                return mid+1
            elif A[mid] <= k:
                start = mid + 1
            elif A[mid] > k:
                end = mid - 1

    def findMedian(self, A):
        i = j = 0
        ctr1 = ctr2 = 0
        total_count = len(A)*len(A[0])
        half_count = total_count//2

        mn = 2**31-1
        mx = -2**31
        for i in range(len(A)):
            mn = min(mn, A[i][0])
            mx = max(mx, A[i][-1])
        start = mn
        end = mx

        while start <= end:
            k = (start+end)//2
            ctr1 = ctr2 = 0
            for i in range(0, len(A)):
                ctr1 += self.count_greater_k(A[i], k)
                ctr2 += self.count_smaller_k(A[i], k)
            if ctr1 > half_count and ctr2 > half_count and ctr1+ctr2 > total_count:
                return k
            if ctr1 == half_count and ctr2 == half_count:
                return k
            elif ctr1 > half_count:
                start = k + 1
            elif ctr1 < half_count:
                end = k - 1
            elif ctr2 < half_count:
                start = k + 1
            elif ctr2 > half_count:
                end = k - 1
        return -1


if __name__ == '__main__':
    A = [
        [1, 1, 1, 2, 3]
    ]

    s = Solution()
    print(s.findMedian(A))
