from typing import List


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A: List):
        answer = []
        li = [ele for ele in A]
        self.permute_rec(A, answer, li)
        return answer

    def permute_rec(self, A: List, ans, li, si=0):
        if si == len(A) - 1:
            ans.append(li.copy())
            return
        for i in range(si, len(A)):
            li[i], li[si] = li[si], li[i]
            self.permute_rec(A, ans, li, si=si+1)
            li[i], li[si] = li[si], li[i]

        return


if __name__ == "__main__":
    s = Solution()
    A = [1, 2, 3]
    print(s.permute(A))
