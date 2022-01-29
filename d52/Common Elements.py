class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        dc = dict()
        for ele in A:
            dc[ele] = dc.get(ele, 0) + 1
        ans = []
        for ele in B:
            if dc.get(ele, 0) > 0:
                dc[ele] = dc[ele] - 1
                ans.append(ele)
        return ans


if __name__ == "__main__":
    A = [1, 2, 2, 1]
    B = [2, 3, 1, 2]
    s = Solution()
    print(s.solve(A, B))
