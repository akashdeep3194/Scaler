class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):        
        max_ele = max(A,B)
        min_ele = min(A,B)

        an = max_ele - min_ele
        
        if A%an == B%an:
            return an

        for i in range(min_ele,1,-1):
            if A % i == B % i:
                ans = i
                break
        return ans

# s = Solution()
# print(s.solve(6816621,8157697))
