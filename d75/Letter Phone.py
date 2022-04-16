from typing import List


class Solution:
    # @param A : string
    # @return a list of strings
    def __init__(self) -> None:
        self.dc = dict()
        self.dc["0"] = ["0"]
        self.dc["1"] = ["1"]
        self.dc["2"] = ["a", "b", "c"]
        self.dc["3"] = ["d", "e", "f"]
        self.dc["4"] = ["g", "h", "i"]
        self.dc["5"] = ["j", "k", "l"]
        self.dc["6"] = ["m", "n", "o"]
        self.dc["7"] = ["p", "q", "r", "s"]
        self.dc["8"] = ["t", "u", "v"]
        self.dc["9"] = ["w", "x", "y", "z"]

    def recfn(self, A, ans: List, si):
        if si == len(A)-1:
            new_ans = []
            for chars in self.dc[A[si]]:
                new_ans.append(chars)
            ans.clear()
            ans.extend(new_ans.copy())
            return

        self.recfn(A, ans, si+1)
        new_ans = []
        for i, ele in enumerate(ans):
            for chars in self.dc[A[si]]:
                new_ans.append(chars+ele)
        ans.clear()
        ans.extend(new_ans.copy())

    def letterCombinations(self, A):
        answer = []
        self.recfn(A, answer, si=0)
        answer.sort()
        return answer


if __name__ == '__main__':
    A = "423"
    s = Solution()
    print(s.letterCombinations(A))
