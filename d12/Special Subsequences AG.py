class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        right = [0 for ele in A]
        ctr = ans = 0
        for i in range(len(A)-1,-1,-1):
            if A[i] == "G":
                ctr += 1
            elif A[i] == "A":
                ans += ctr
                ans = ans%(10**9 + 7)
        return ans%(10**9 + 7)

# s = Solution()
# print(s.solve("asdhgsdhgasgssg".upper()))