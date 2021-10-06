class Solution:
	# @param A : integer
	# @return a list of list of integers
    def generateMatrix(self, A):

        m = A
        n = A

        ans = [[0 for _ in range(m)] for _ in range(n)]

        val = 1
        i = 0
        j = 0


        while(n>1 and m>1):
            for k in range(m-1):
                ans[i][j] = val
                j+=1
                val+=1
            for k in range(n-1):
                ans[i][j] = val
                val+=1
                i+=1
            for k in range(m-1):
                ans[i][j] = val
                val+=1
                j-=1
            for k in range(n-1):
                ans[i][j] = val
                val+=1
                i-=1
            i+=1
            j+=1
            n = n-2
            m = m-2
        if n==1:
            for k in range(m):
                ans[i][j] = val
                val += 1
                j+=1
            m=0
        if m==1:
            for k in range(n):
                ans[i][j] = val
                val += 1
                i+=1
        return ans

# s = Solution()
# mat = s.generateMatrix(5)
# for ele in mat:
#     print(ele)
#     print()
