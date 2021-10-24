import sys

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        d = dict()
        odd_c = 0

        for ele in A:
            d[ele] = d.get(ele,0)+1
        
        for k,v in d.items():
            if v&1 == 1:
                odd_c += 1
                if odd_c >1:
                    return 0
        return 1

# s = Solution()
# print(s.solve("vnpbeutxfqxriiajoejjmtjcx"))
