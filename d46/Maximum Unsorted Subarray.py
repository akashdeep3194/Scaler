class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        B = sorted(A)
        if A[0] != B[0] and A[-1] != B[-1]:
            return [0, len(A)-1]
        si = 0
        ei = len(A)-1

        for i in range(len(A)):
            if A[i] == B[i]:
                si += 1
            else:
                break
        if si == len(A):
            return [-1]
        for j in range(len(A)-1, -1, -1):
            if A[j] == B[j]:
                ei -= 1
            else:
                break
        return [si, ei]


if __name__ == '__main__':
    s = Solution()
    print(s.subUnsort([1, 2, 3]))
