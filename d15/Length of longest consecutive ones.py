class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)

        pfr = [0 for _ in range(n)]
        pfl = [0 for _ in range(n)]

        total_ones = 0

        ans = 0


        pfl[0]= int(A[0])
        total_ones = pfr[n-1] = int(A[n-1])

        for i in range(n-2,-1,-1):
            if A[i] == '1':
                pfr[i] = pfr[i+1] + 1
                total_ones += 1
            else:
                pfr[i] == 0

        if total_ones == n:
            return n
        if total_ones <= 1:
            return total_ones

        for i in range(0,n):
            ele = A[i]
            if ele == '0':
                pfl[i] = 0

                if i == 0:
                    left_ones = 0
                else:
                    left_ones = pfl[i-1]
                if i == n-1:
                    right_ones = 0
                else:
                    right_ones = pfr[i+1]

                temp = left_ones+right_ones

                if temp<total_ones:
                    temp += 1

                ans = max(ans,temp)


            else:
                pfl[i] = pfl[i-1]+1

        return ans

# s = Solution()
# print(s.solve("010100110101"))
