class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        ses = []
        ts = s = 0
        ans = 0

        for i in range(len(A)-1,-1,-1):

            if i%2 == 0:
                s += A[i]

            ses.append(s)
            ts += A[i]
        ses = ses[::-1]
        pos =  0

        for i in range(len(A)):

            if i%2 == 0:
                os = pos + ses[i] - A[i]
                es = ts - os - A[i]

            else:
                pos += A[i]
                os = pos + ses[i] - A[i]
                es = ts - os - A[i]

            if os == es:
                ans += 1

        return ans

# A=[2, 1, 6, 4]
# s = Solution()
# print(s.solve(A))
