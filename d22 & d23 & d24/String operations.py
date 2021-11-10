class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        str = ""
        ans = []
        A = list(A)
        A.extend(A)

        for i,ele in enumerate(A):
            if 65<=ord(ele)<=90:
                A[i] = ""
            if ele in ('a','e','i','o','u'):
                A[i] = "#"
        for ele in A:
            str += ele
        return str





# s = Solution()
# print(s.solve("AbcaZeoB"))
