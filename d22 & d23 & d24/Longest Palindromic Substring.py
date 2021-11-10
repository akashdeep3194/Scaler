class Solution:
    # @param A : string
    # @return a strings
    def expand(self,si,ei,s):
        ctr = 0
        while si>=0 and ei<=len(s)-1:
            
            if s[si] == s[ei]:
                ctr += 1
                si -= 1
                ei += 1
            else:
                return s[si+1:ei]
        return s[si+1:ei]

    def longestPalindrome(self, A):
        ans = ""
        for i in range(len(A)):
            ctr_odd = self.expand(i,i,A)
            ctr_even = self.expand(i,i+1,A)
            if len(ans)<len(ctr_odd)>len(ctr_even):
                ans = ctr_odd
            elif len(ans)<len(ctr_even)>len(ctr_odd):
                ans = ctr_even
        return ans

# s = Solution()
# print(s.longestPalindrome("aaaabaaa"))
