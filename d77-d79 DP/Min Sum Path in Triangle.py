class Solution:
    # @param A : list of list of integers
    # @return an integer
    def recfn(self, A, si):
        if len(A)-1 == si:
            ans = []
            for ele in A[si]:
                ans.append(ele)
            return ans

        sa = self.recfn(A, si+1)
        k = 0
        ans = []
        for i in range(len(sa)-1):
            ans.append(min(sa[i], sa[i+1]) + A[si][k])
            k += 1
        return ans

    def minimumTotal(self, A):
        return self.recfn(A, si=0)[0]


if __name__ == '__main__':
    A = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    s = Solution()
    print(s.minimumTotal(A))
