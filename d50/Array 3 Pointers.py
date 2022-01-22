class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        i = j = k = 0
        ans = max(abs(A[0]-B[0]), abs(A[0]-C[0]), abs(B[0]-C[0]))

        while i < len(A) and j < len(B) and k < len(C):
            a = abs(A[i]-B[j])
            b = abs(B[j]-C[k])
            c = abs(A[i]-C[k])
            ans = min(max(a, b, c), ans)
            if ans == 0:
                return ans
            elif C[k] > A[i] < B[j]:
                i += 1
            elif C[k] > B[j] < A[i]:
                j += 1
            elif A[i] > C[k] < B[j]:
                k += 1
            else:
                if A[i] == B[j]:
                    i += 1
                else:
                    k += 1

        return ans
