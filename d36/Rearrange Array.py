class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
        n = len(A)
        for i,ele in enumerate(A):
            A[i] *= n
        
        for i,ele in enumerate(A):
            rem = A[A[i]//n]//n
            A[i] += rem
        for i,ele in enumerate(A):
            A[i] = A[i]%n

if __name__ == '__main__':
    s = Solution()
    A = [1,2,0,4,5,3]
    print(A)
