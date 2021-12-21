class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def divide(self, A, B):
        sign = 1
        if A<0 and B<0:
            A = abs(A)
            B = abs(B)
        if A>0 and B<0:
            B = abs(B)
            sign = -1
        if A<0 and B>0:
            A = abs(A)
            sign = -1

        if B == 1:
            A = A*sign
            if A>= 2**31-1:
                return 2**31-1 
            elif A< -2**31:
                return 2**31
            return A
        num = 0

        for i in range(31,-1,-1):
            if (B<<i)<=A:
                num += 2**i
                A = A - (B<<i)
            if A<B:
                break
        num = num*sign

        if num >= 2**31-1:
            return 2**31-1
        elif num<-2**31:
            return 2**31-1

        return num

if __name__ == '__main__':
    s = Solution()
    print(s.divide(-2147483648,1))
