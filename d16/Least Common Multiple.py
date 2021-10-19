class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def LCM(self, A, B):
        min_ele = min(A,B)
        for ele in range(min_ele,A*B+1):
            if ele%A == ele%B == 0:
                return ele
s = Solution()
print(s.LCM(4,6))
