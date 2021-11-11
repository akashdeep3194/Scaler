class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def checkbit(self,x):
        s=0
        ans = []
        while 2**s<=x :
            if (2**s & x) == 2**s:
                ans.append(s)
            s+=1
        return ans

    def solve(self, A, B):
        n = len(A)
        i=0
        while i < (1<<n):
            set_bits = self.checkbit(i)
            s = 0
            for bit in set_bits:
                s +=A[bit]
            if s == B:
                return 1
            i += 1
        return 0

# A=[1,20,13,4,5]

# B=18

# s = Solution()
# print(s.solve(A,B))
# # print(s.checkbit(12))
