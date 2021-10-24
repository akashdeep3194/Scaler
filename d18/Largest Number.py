from math import log10
from typing import List
from functools import cmp_to_key
def comp(a,b):
    a = str(a)
    b = str(b)

    if a + b > b + a:
        return 1
    elif a + b < b + a:
        return -1
    else:
        return 0

class Solution:
    # @param A : tuple of integers
    # @return a strings

    def largestNumber(self, A):
        arr = sorted(A,key = cmp_to_key(comp),reverse=True)
        ans = ""
        ret = 0
        for ele in arr:
            ans += str(ele)
            if ele != 0:
                ret = 1
        if ret == 0:
            return "0"
        return ans

# s = Solution()
# A = [ 931, 94, 209, 448, 716, 903, 124, 372, 462, 196, 715, 802, 103, 740, 389, 872, 615, 638, 771, 829, 899, 999, 29, 163, 342, 902, 922, 312, 326, 817, 288, 75, 37, 286, 708, 589, 975, 747, 743, 699, 743, 954, 523, 989, 114, 402, 236, 855, 323, 79, 949, 176, 663, 587, 322 ]
# print(s.largestNumber(A))
