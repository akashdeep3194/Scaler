from collections import deque


class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        stack = deque()
        ans = ""
        for ele in A:
            if ele == ans:
                stack.pop()
            else:
                stack.append(ele)
            if len(stack) == 0:
                ans = ""
            else:
                ans = stack[-1]
        ans = ""
        while len(stack) > 0:
            ans = stack.pop() + ans

        return ans


if __name__ == "__main__":
    s = Solution()
    A = "abccbc"
    print(s.solve(A))
