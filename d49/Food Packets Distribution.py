class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def canBeAllocated(self, B, A, C):
        for ele in A:
            if ele < C:
                return False
            k = 1
            if B == 0:
                return True
            while ele//k >= C:
                B -= 1
                if B == 0:
                    return True
                k += 1
        return False

    def solve(self, A, B):
        sm = 0
        for ele in A:
            sm += ele
        start = 0
        stop = min(A)
        if B > sm:
            return 0
        while start <= stop:
            mid = (start+stop)//2
            if self.canBeAllocated(B, A, mid):
                ans = mid
                start = mid + 1
            else:
                stop = mid - 1
        return int(ans)


if __name__ == "__main__":
    s = Solution()
    A = [900, 90, 90]
    B = 7

    print(s.solve(A, B))
