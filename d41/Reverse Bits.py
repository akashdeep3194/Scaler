class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        n = 31
        k = 0
        ans  = 0
        while n>=0:
            ans += int((2**n)*((A&2**k)/(2**k)))
            n -= 1
            k += 1
        return ans
