class Solution:
    # @param A : string
    # @return an integer
    def recfn(self, A):

        for i in range(len(A)):
            for j in range(i+1, len(A)):
                s = A[:i]+A[i+1:j]+A[j+1:]
                ss = 0
                for ele in s:
                    if ss == 1 and ele == A[j]:
                        return 1
                    if ele == A[i]:
                        ss = 1
        return 0

    def anytwo(self, A):
        return self.recfn(A)


if __name__ == '__main__':
    A = "paxbmab"
    s = Solution()
    print(s.anytwo(A))
