class Solution:
    # @param A : list of integers
    # @return an integer
    def solveHelper(self,A,l,r):
        if l == r:
            return 0

        m = (r-l+1)//2

        ans = 0

        x = self.solveHelper(A,l,l+m-1)
        y = self.solveHelper(A,l+m,r)

        temp = [0]*(r-l+1)
        
        i = l
        k = 0
        j = l+m
        
        while i<=l+m-1 and  j<=r:
            if A[i]<=A[j]:
                temp[k] = A[i]
                i += 1
            else:
                temp[k] = A[j]
                j += 1
                ans += (l+m-i)%(10**9 + 7)
            k += 1

        while i<=l+m-1:
            temp[k] = A[i]
            i += 1
            k += 1
        
        while j<=r:
            temp[k] = A[j]
            j += 1
            k += 1
    
        for i in range(len(temp)):
            A[i+l] = temp[i]

        return (ans + x + y)%(10**9 + 7)

            
    def solve(self, A):
        ans = self.solveHelper(A,0,len(A)-1)
        return ans

    # def solvex(self,A):
    #     count = 0
        
    #     for i,ele in enumerate(A):
    #         for j in range(i+1,len(A)):
    #             if A[i] > A[j]:
    #                 count += 1
    #     return count

if __name__ == '__main__':
    A = [1, 5, 4, 8, 7, 6, 1, 2, 3, 0, 5]
    s = Solution()
    # print(s.solvex(A))
    print(s.solve(A))
