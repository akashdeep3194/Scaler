class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        arr = []
        arr.append(B)
        for ele in C:
            if ele == 0:
                arr.pop()
            else:
                arr.append(ele)
        return arr[-1]
