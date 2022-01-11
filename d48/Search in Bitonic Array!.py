class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def BinarySearch(self, A, l, r, b, order=1):
        while l <= r:
            mid = l + (r-l+1)//2
            if A[mid] == b:
                return mid
            elif A[mid] > b:
                if order == 1:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if order == 1:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

    def BitonicSearch(self, arr, l, r):
        while l <= r:
            mid = l + (r-l+1)//2
            if arr[mid] > arr[mid-1]:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

    def solve(self, A, B):

        if A[0] == B:
            return 0
        if A[-1] == B:
            return len(A) - 1

        start = 0
        end = len(A)-1

        bitonic_index = self.BitonicSearch(A, 0, len(A)-1)
        sa1 = sa2 = -1
        sa1 = self.BinarySearch(A, 0, bitonic_index, B)
        sa2 = self.BinarySearch(A, bitonic_index+1, len(A)-1, B, -1)
        return max(sa1, sa2)


if __name__ == '__main__':
    s = Solution()
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
    B = 12
    print(s.solve(A, B))
