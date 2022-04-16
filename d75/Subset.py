from typing import List


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def recfn(self, A, ans, si, li: List):
        if si == len(A):
            ans.append(li.copy())
            return
        li.append(A[si])
        self.recfn(A, ans, si+1, li)
        li.pop()
        self.recfn(A, ans, si+1, li)
        return

    def subsets(self, A):
        answer = []
        A.sort()
        self.recfn(A, ans=answer, si=0, li=[])
        return sorted(answer)


if __name__ == "__main__":
    s = Solution()
    A = [4, 12, 13]
    print(s.subsets(A))
