class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def findele(self, ele, arr, start=0):
        end = len(arr) - 1
        ans = -1
        while start <= end:
            mid = (start+end)//2
            if arr[mid] == ele:
                return mid
            if arr[mid] > ele:
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        return ans

    def canKCowsBePlacedAtDist(self, arr, k, dist):
        i = 0
        ele = arr[i] + dist
        ctr = 1
        for i in range(1, len(arr)):
            if arr[i] >= ele:
                ele = arr[i] + dist
                ctr += 1
                if ctr >= k:
                    return True
        return False

    def solve(self, A, B):
        start = 1
        ans = -1
        A.sort()
        stop = A[-1]-A[0]
        while start <= stop:
            mid = (start+stop)//2
            if self.canKCowsBePlacedAtDist(A, B, mid):
                ans = mid
                start = mid + 1
            else:
                stop = mid - 1
        return ans


if __name__ == '__main__':
    s = Solution()
    A = [1, 2, 3, 4, 5]
    B = 3
    print(s.solve(A, B))
