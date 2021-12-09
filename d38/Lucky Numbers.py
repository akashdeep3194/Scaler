class Solution:

    # @param A : integer
    # @return an integer

    def solve(self, A):
        spf = [0 for _ in range(A+1)]

        for i in range(2,A+1):

            if spf[i] == 0:
                j = i*2
                while j<=A:
                    if spf[j] <= 2:
                        spf[j] += 1
                    j += i


        ctr = 0

        for ele in spf:
            if ele == 2:
                ctr += 1
        return ctr

if __name__ == '__main__':
    s = Solution()
    print(s.solve(12))
