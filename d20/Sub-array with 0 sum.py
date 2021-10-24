class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        pf = []
        sum = 0
        d = dict()
        for i,ele in enumerate(A):
            sum += ele
            pf.append(sum)
            if pf[i] == 0:
                return 1
            d[sum] = d.get(sum,0)+1
            if d[sum]>1:
                return 1
        return 0

# s = Solution()
# A = [ -1, 1 ]
# print(s.solve(A))
