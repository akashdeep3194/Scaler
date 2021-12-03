class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):
        if A==0:
            return A
        if B==0:
            return 1
        if B==1:
            return A%C
        
        if B%2 == 0:
            sa = pow(A,B//2,C)
            ans = (sa*sa)%C
        else:
            sa = pow(A,B//2,C)
            ans = ((sa*sa)%C*(A%C))%C
        
        return ans
