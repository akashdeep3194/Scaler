class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        N = len(A)
        freq_a = freq_b = 0
        num_a = num_b = 0
        for ele in A:
            if ele == num_a:
                freq_a += 1

            elif ele == num_b:
                freq_b += 1

            elif freq_a == 0:
                num_a = ele
                freq_a = 1
            elif freq_b == 0:
                num_b = ele
                freq_b = 1

            else:
                freq_b -= 1
                freq_a -= 1

        ctra = ctrb = 0
        for ele in A:
            if ele == num_a:
                ctra += 1
            if ele == num_b:
                ctrb += 1
        if ctra > N//3:
            return num_a
        elif ctrb > N//3:
            return num_b
        else:
            return -1
# s = Solution()
# print(s.repeatedNumber([ 1000441, 1000441, 1000994 ]))
