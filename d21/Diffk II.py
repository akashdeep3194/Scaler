class Solution:
    # @param A : tuple of integers
    # # @param B : integer
    # # @return an integer
    def diffPossible(self, A, B):
        d = dict()
        for ele in A:
            d[ele] = d.get(ele,0) + 1
        for ele in A:
            find = ele - B
            x = d.get(find,0)
            if x != 0:
                if find != ele:
                    return 1
                else:
                    if x>1:
                        return 1
        return 0

# s = Solution()
# A = [1, 5, 3]
# k = 2
# print(s.diffPossible(A,k))
