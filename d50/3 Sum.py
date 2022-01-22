class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def pairClosest(self, A, B):
        i = 0
        j = len(A) - 1
        ans = A[0]+A[1]
        if B < A[0]+A[1]:
            return A[0]+A[1]
        if B > A[-1]+A[-2]:
            return A[-1]+A[-2]
        while i < j:
            if A[i]+A[j] == B:
                return B

            elif A[i]+A[j] > B:
                if abs(A[i]+A[j]-B) < abs(ans-B):
                    ans = A[i]+A[j]
                j -= 1

            elif A[i]+A[j] < B:
                if abs(A[i]+A[j]-B) < abs(ans-B):
                    ans = A[i]+A[j]
                i += 1
        return ans

    def threeSumClosest(self, A, B):
        A.sort()
        if len(A) == 1:
            return A[0]
        if len(A) == 2:
            return min(abs(A[0]+A[1]-B), abs(A[1]-B), abs(A[0]-B))
        ans = A[0]+A[1]+A[2]
        for i in range(len(A)-2):
            find = B-A[i]
            sa = self.pairClosest(A[i+1:], find)
            if abs(sa + A[i]-B) < abs(ans-B):
                ans = sa+A[i]
                if ans == B:
                    return ans
        return ans


if __name__ == '__main__':
    s = Solution()
    A = [-1, 2, 1, -4]
    B = 1
    print(s.threeSumClosest(A, B))
