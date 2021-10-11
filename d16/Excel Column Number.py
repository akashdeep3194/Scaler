from typing import AnyStr


class Solution:
	# @param A : string
	# @return an integer
    def titleToNumber(self, A):
        ans = 0
        A = A[::-1]
        for ind,ele in enumerate(A):
            ele = ord(ele) - 64
            i = 26**ind
            ans += ele*i
        return ans



# s = Solution()

# print(s.titleToNumber("AB"))
