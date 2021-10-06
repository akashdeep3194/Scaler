class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        n = len(A)
        m = len(A[0])

        ans = []


        i = 0
        for j in range(m):        
            li = [0 for ele in range(min(n,m))]
            i=0
            jj = j
            while i<n and jj>=0:
                li[i] = (A[i][jj])
                i+=1
                jj-=1
            ans.append(li)

        j = m-1

        for i in range(1,n):        
            li = [0 for ele in range(min(n,m))]
            j=m-1
            ii = i

            while ii<n and j>=0:
                li[m-1-j] = (A[ii][j])
                ii+=1
                j-=1

            ans.append(li)
        return ans


# A = [[1, 2, 3], [4, 5, 6]]

# s = Solution()

# print(s.diagonal(A))

