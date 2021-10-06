class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n =  len(A)
        m = len(A[0])

        k = m-1
        i = 0

        ans =  -1

        while k>=0 and i<n:
            if A[i][k] == B:
                ans = (i+1)*1009+k+1
                k-=1
            elif A[i][k]<B:
                if ans != -1:
                    return ans
                i += 1
            else:
                k -= 1
        return ans
