class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        s = i = 0
        n = len(A)
        
        while i<n:
            ele = A[i]
            if ele == i:
                i+=1
            elif A[ele] == i:
                s+=1
                A[ele],A[i] = A[i],A[ele]
                i+=1
            else:
                A[ele],A[i] = A[i],A[ele]
                s+=1
        return s
                
if __name__ == '__main__':
    s = Solution()
    print(s.solve([5,0,3,2,4,1]))
