from math import log2
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = B        
        if A == 0:
            return 2**n - 1
        k = int(log2(A))
        x = 0

        while n>0 and k>=0:
            if A&2**k == 2**k:
                x += 2**k
                n -= 1
            k -= 1
        
        k = 0
        while n>0:
            if A&2**k == 0:
                x += 2**k
                n  -= 1
            k += 1
        return x

if __name__ == '__main__':
    s = Solution()
    print(s.solve(3,3))
