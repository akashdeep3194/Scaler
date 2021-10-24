class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def getSum(self, A, B, C):
        d = dict()
        sum = 0
        ret = -1
        for i,ele in enumerate(C):
            d[ele] = d.get(ele,0)+1
        for k,v in d.items():
            if v == B:
                ret = 0
                sum += k
        if ret == -1:
            return -1
        return sum

s = Solution()

# A=3
# B=2
# C=[0, 0, 1]
# print(s.getSum(A,B,C))
