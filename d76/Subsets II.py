class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def recfn(self, A, ans, li, si=0):
        if si == len(A):
            if li not in ans:
                ans.append(li.copy())
            return

        li.append(A[si])
        self.recfn(A, ans, li, si+1)
        li.pop()
        self.recfn(A, ans, li, si+1)
        return

    def subsetsWithDup(self, A):
        answer = []
        li = []
        A.sort()
        self.recfn(A, answer, li)
        answer.sort()
        return answer


if __name__ == '__main__':
    A = [1, 2, 2]
    s = Solution()
    print(s.subsetsWithDup(A))
