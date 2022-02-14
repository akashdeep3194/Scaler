from collections import deque


class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        q = deque()
        dc = dict()
        ans = ""

        for ele in A:
            dc[ele] = dc.get(ele, 0) + 1
            if dc[ele] > 1:
                while len(q) > 0 and dc[q[-1]] > 1:
                    q.pop()
                if len(q) == 0:
                    ans = ans+"#"
                else:
                    ans = ans + q[-1]
            else:
                q.appendleft(ele)
                x = q[-1]
                ans = ans+x
        return ans
