import sys

class Solution:
    	# @param A : integer
	# @return an integer
    def colorful(self, A):
        a = str(A)
        a = list(map(int,list(a)))

        d = dict()

        for i in range(len(a)):
            prod = 1
            for j in range(i,len(a)):
                prod = prod*a[j]
                d[prod] = d.get(prod,0)+1

        for k,v in d.items():
            if v>1:
                return 0
        return 1

# s = Solution()
# print(s.colorful(1234))
