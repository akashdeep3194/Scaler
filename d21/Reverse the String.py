class Solution:
    # @param A : string
    # @return a strings
    def rev_word(self,rev,i,j):
        ans = ""
        for z in range(j,i-1,-1):
            ans += rev[z]
        return ans

    def solve(self, A):
        rev = A[::-1]
        ans = ""
        rev = rev.strip()
        i=0
        j=0
        while i<len(rev) and j<len(rev)-1:
            if rev[j+1] == " ":
                ans += self.rev_word(rev,i,j) + " "
                j+=1
                i=j
            j+=1
        ans += self.rev_word(rev,i,j)
        return ans
s = Solution()
A = "cjaztsibp kw zxacowfkk l khry fmxeyg gmxqumysg wveh "
print(s.solve(A))
