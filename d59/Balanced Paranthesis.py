from collections import deque


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        stack = deque()
        for ele in A:
            if ele in ("}", ")", "]"):
                if len(stack) == 0:
                    return 0
                else:
                    ans = stack.pop()
                if ele == "}":
                    if ans != "{":
                        return 0
                elif ele == "]":
                    if ans != "[":
                        return 0
                elif ele == ")":
                    if ans != "(":
                        return 0
            else:
                stack.append(ele)
        if len(stack) == 0:
            return 1
        else:
            return 0


if __name__ == "__main__":
    s = Solution()
    A = "{([])}"
    print(s.solve(A))
