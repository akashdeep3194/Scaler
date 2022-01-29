class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        dc = dict()
        for ele in A:
            dc[ele] = dc.get(ele, 0) + 1

        ctr = 0

        for k, v in dc.items():
            if v % 2 != 0:
                ctr += 1
            if ctr == 2:
                return 0
        return 1


if __name__ == "__main__":
    s = Solution()
    A = "abbaee"
    print(s.solve(A))
