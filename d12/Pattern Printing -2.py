class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):

        ans = []

        for i in range(A):
            li=[]
            k=A
            for j in range(A):
                if j<A-1-i:
                    li.append(0)
                else:
                    li.append(k)
                k -= 1
            ans.append(li)
        return ans

# s=Solution()

# print(s.solve(3))   