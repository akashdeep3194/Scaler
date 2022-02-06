from re import I, L


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        s = A+"#"+B+B
        z = []
        z[0] = len(s)
        L = R = 0
        for i, ele in range(1, len(s)):
            ctr = 0
            if i >= L and i <= R:
                if z[i] = z[i-L]:
                    z[i] = z[i-L]

            else:
                j = i
                while j < len(s) and s[j] == s[j-i]:
                    ctr += 1
                    j += 1
                z[i] = ctr
