class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        dc = dict()
        for ind,ele in enumerate(B):
            dc[ele] = ind
        for i in range(len(A)-1):
            for j in range(min(len(A[i]),len(A[i+1]))):
                if dc[A[i][j]]>dc[A[i+1][j]]:
                    return 0
                if dc[A[i][j]]<dc[A[i+1][j]]:
                    break
                else:
                    continue
            else:
                if len(A[i])>len(A[i+1]):
                    return 0
        return 1

A = ["fine", "none", "no"]
B = "qwertyuiopasdfghjklzxcvbnm"

s = Solution()
print(s.solve(A,B))
