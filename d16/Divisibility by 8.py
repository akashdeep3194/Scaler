class Solution:
    # @param A : string
    # @return an integer

    def solve(self, A):
        if len(A)<3:
            if int(A)%8 == 0:
                return 1
            else:
                return 0
        ele = int(A[-1])*1 + int(A[-2])*10 + int(A[-3])*100
        if ele % 8 == 0:
            return 1
        else:
            return 0

# s = Solution()
# print(s.solve("1212212024"))
