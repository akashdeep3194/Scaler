class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            return -1
        ans = []

        for i, ele in enumerate(A):
            li = []

            for j,el in enumerate(ele):
                li.append(el-B[i][j])
            ans.append(li)

        return ans

# s = Solution()

# print(s.solve([[1,2,3],[3,4,5]],[[1,2,1],[4,5,6]]))
