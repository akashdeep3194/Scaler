class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        d = dict()
        for ind,ele in enumerate(A):
            find = B-ele
            if d.get(find,-1) != -1:
                return [d[find]+1, ind+1]
            if d.get(ele,-1) == -1:
                d[ele] = ind
        return []
# s = Solution()
# print(s.twoSum((2,7,11,15),9))
