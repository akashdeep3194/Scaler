class Solution:
    # @param A : list of integers
    # @return a list of integers

    def checkSetBit(self, x: int) -> int:
        ctr = 0

        while x > 0:
            if x & 1 == 1:
                return ctr

            x = x >> 1
            ctr += 1

        return -1

    def solve(self, A):
        a = A
        t = 0

        for ele in a:
            t = ele ^ t

        setBit = self.checkSetBit(t)

        if setBit < 0:
            return -1

        ans_a = ans_b = 0

        for ele in a:
            if ele >> setBit & 1:
                ans_a = ans_a ^ ele
            else:
                ans_b = ans_b ^ ele

        ret_arr = [min(ans_b, ans_a), max(ans_b, ans_a)]
        return ret_arr


s = Solution()
print(s.solve([186, 256, 102, 377, 186, 377]))
