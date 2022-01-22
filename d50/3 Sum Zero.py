class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def pairSum(self, A, B):
        i = 0
        j = len(A) - 1
        ans = []

        while j > i:
            if A[i]+A[j] == B:
                ans.append([A[i], A[j]])
                i += 1
                j -= 1
            elif A[i] + A[j] > B:
                j -= 1
            elif A[i]+A[j] < B:
                i += 1
        return ans

    def threeSum(self, A):
        A.sort()
        ans = []

        for i in range(0, len(A)):
            B = A[i]*-1
            sa = self.pairSum(A, B)
            ans.extend(sa)
        return ans


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def pairSum(self, A, B):
        i = 0
        j = len(A) - 1
        ans = []

        while j > i:
            if A[i]+A[j] == B:
                ans.append([A[i], A[j]])
                i += 1
                j -= 1
            elif A[i] + A[j] > B:
                j -= 1
            elif A[i]+A[j] < B:
                i += 1
        return ans

    def threeSum(self, A):
        A.sort()
        ans = []

        for i in range(0, len(A)):
            B = A[i]*-1
            sa = self.pairSum(A, B)
            ans.extend(sa)
        return ans


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def pairSum(self, A, B):
        i = 0
        j = len(A) - 1
        s = set()

        while j > i:
            if A[i]+A[j] == B:
                s.add((B*-1, A[i], A[j]))
                i += 1
                j -= 1
            elif A[i] + A[j] > B:
                j -= 1
            elif A[i]+A[j] < B:
                i += 1
        return s

    def threeSum(self, A):
        A.sort()
        ans = []

        for i in range(0, len(A)):
            if i > 0 and A[i] == A[i-1]:
                continue
            B = A[i]*-1
            sa = list(self.pairSum(A[i+1:], B))
            ans.extend(sa)
        return ans


if __name__ == "__main__":
    s = Solution()
    A = [-1, 0, 1, 2, -1, 4]
    print(s.threeSum(A))

    b = 5
    arr = [1, 0, -2, 4, -4, 1, -1, -4, 3, 4, -1, -1, -3]
    arr.sort()
    print(s.pairSum(arr, b))
