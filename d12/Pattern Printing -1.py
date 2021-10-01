class Solution:
    # @param A : integer
    # @return a list of list of integers

    def solve(self, A):
        arr = []

        for i in range(A):
            li = []        
            for j in range(A):
                if j<=i:
                    li.append(j+1)
                else:
                    li.append(0)
            arr.append(li)
        return arr

# s = Solution()
# print(s.solve(3))
