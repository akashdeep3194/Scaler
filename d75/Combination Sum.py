class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        A = list(set(A))
        A.sort()
        answer = []
        li = []
        self.recfn(A, B, answer, li)
        return answer

    def recfn(self, A, B, ans, li, si=0):
        if B == 0:
            ans.append(li.copy())
            return True
        elif B < 0:
            return False
        if si >= len(A):
            return False

        li.append(A[si])
        self.recfn(A, B-A[si], ans, li, si)
        li.pop()
        self.recfn(A, B, ans, li, si=si+1)
        return


if __name__ == "__main__":
    s = Solution()
    A = [8, 10, 6, 11, 1, 16, 8]
    B = 28
    for ele in s.combinationSum(A, B):
        print(ele)
