class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer

    def fastPower(self,a,b,m):

        ans = 1


        for i in range(b):
            ans = ans%m*a%m
            ans = ans%m
        return ans


    def findMod(self, A, B):

        ans = 0
        sm_ans = 1

        for i in range(len(A)-1,-1,-1):
            ele = int(A[i])
            ans += (ele%B*sm_ans)%B
            ans = ans%B
            sm_ans = (10%B*sm_ans)%B
        return ans
# s = Solution()
# print(s.findMod("143",2))
