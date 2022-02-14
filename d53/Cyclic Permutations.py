class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        s = A+"#"+B+B[:len(B)-1]
        z = [0 for _ in range(len(s))]
        z[0] = len(s)
        L = R = ans = 0
        for i in range(1, len(s)):
            ctr = 0
            if i >= L and i <= R:
                if s[i] == s[i-L]:
                    if z[i-L] < R-i+1:
                        z[i] = z[i-L]
                    else:
                        z[i] = R-i+1
                        k = R+1
                        while k < len(s) and s[k] == s[k-i]:
                            ctr += 1
                            k += 1
                        z[i] = ctr + z[i]
                        L = i
                        R = k-1
            else:
                j = i
                while j < len(s) and s[j] == s[j-i]:
                    ctr += 1
                    j += 1
                z[i] = ctr
                R = j-1
                L = i
            if z[i] == len(B):
                ans += 1
        return ans
