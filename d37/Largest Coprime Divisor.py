class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self,A,B):
        if A>B:
            A,B = B,A

        while A!=0:
            B = B%A
            if A>B:
                A,B = B,A

        return B

            
    def cpFact(self, A, B):

        gcd_val = self.gcd(A,B)
        X = A//gcd_val
        
        gcd_val = self.gcd(X,B)
       
        while gcd_val != 1 and X != 1:
            X = X//gcd_val
            gcd_val = self.gcd(X,B)

        return X

            
if __name__ == '__main__':
    s=Solution()
    print(s.cpFact(168,36))
