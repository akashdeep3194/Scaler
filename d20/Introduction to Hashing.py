class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        A = sorted(A)
        B = sorted(B)
        ans = []
        i = j = 0
        while i<len(A) and j<len(B):
            if A[i] == B[j]:
                ans.append(A[i])
                i+=1
                j+=1
            elif A[i]<B[j]:
                i+=1
            else:
                j+=1
        return ans

s = Solution()
print(s.solve([ 17, 12, 5, 3, 14, 13, 3, 2],[ 19, 16, 8, 7, 12, 19, 10, 13, 8, 20, 16, 15, 4, 12, 3, 14, 14]))
# 1 2 4 10
# 2 3 6 10 10
