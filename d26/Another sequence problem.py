from typing import AnyStr


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        # if A == 2:
        #     return A
        # if A <= 1:
        #     return 1
        # sa = self.solve(A-1)+self.solve(A-2)+self.solve(A-3)+A

        # return sa

        arr = [1,1,2]
        i = 3
        s = 4
        ans = 4
        if A<= 1:
            return 1
        if A == 2:
            return 2
        while i<=A:
            ans = i + s
            s = s - arr[0] + ans
            arr[0] = arr[1]
            arr[1] = arr[2]
            arr[2] = ans

            i += 1
        return ans

s = Solution()
s.solve(5)
