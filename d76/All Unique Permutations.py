class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def recfn(self, A, ans, li, si=0):
        if si == len(A):
            # if li not in ans:
            ans.append(li.copy())
            return

        swaps = dict()

        for i in range(si, len(A)):
            if not swaps.get(li[i]):
                swaps[li[i]] = 1
                li[i], li[si] = li[si], li[i]
                self.recfn(A, ans, li, si+1)
                li[i], li[si] = li[si], li[i]
            else:
                continue

    def permute(self, A):
        A.sort()
        answer = []
        li = [ele for ele in A]
        self.recfn(A, answer, li)
        answer.sort()
        return answer


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6, 7, 8]
    s = Solution()
    print(s.permute(A))
