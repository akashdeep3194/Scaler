from math import log2

class Solution:
    # @param A : integer
    # @return an integer

    def checkCount(self,num):

        count = 0

        while num>0:
            if num&1 == 1:
                count += 1
            num = num>>1

        return count

    def solve(self, A):
        if A == 1:
            return 1
        if A == 0:
            return 0
        n = int(log2(A))
        nm = 2**n
        si = nm^A
        sa = self.solve(si)
        
        ans = (int((2**(n-1))*(n)%(10**9 + 7)) + sa)%(10**9 + 7) + A%(10**9 + 7) - 2**n + 1
        
        return ans%(10**9 + 7)

if __name__ == '__main__':
    s = Solution()
    print(s.solve(20))
