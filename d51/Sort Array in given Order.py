class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        A.sort()
        dc = dict()
        ctr = 0
        ans = []
        for ele in A:
            dc[ele] = dc.get(ele, 0) + 1
        for ele in B:
            ctr = dc.get(ele, 0)
            while ctr > 0:
                ans.append(ele)
                dc[ele] -= 1
                ctr -= 1
        for ele in A:
            if dc[ele] > 0:
                ans.append(ele)
        return ans


if __name__ == "__main__":
    s = Solution()
    A = [10, 2, 18, 16, 16, 16]
    B = [3, 13, 2, 16, 4, 19]
    print(s.solve(A, B))
