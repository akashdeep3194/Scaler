class Solution:
    # @param A : integer
# @return a list of list of integers
    def generateMatrix(self, A):
        n = A
        ctr = 1
        A = [[1 for _ in range(n)] for _ in range(n)]
        i = 0
        round = 0
        while round < int(n//2):
            i = round
            j = round

            while(j<n-1-round):
                A[i][j] = ctr
                ctr+=1
                j+=1
            while(i<n-1-round):
                A[i][j] = ctr
                i+=1
                ctr+=1
            while j>round:
                A[i][j] = ctr
                j-=1
                ctr+=1

            while i>round:
                A[i][j] = ctr
                ctr+=1
                i-=1

            round += 1

        if n%2>0 and n>1:
            A[i+1][j+1] = ctr
        return A

if __name__ == '__main__':
    s = Solution()
    print(s.generateMatrix(1))
