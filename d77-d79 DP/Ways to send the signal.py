from sys import setrecursionlimit
setrecursionlimit(10**6)


class Solution:
    # @param A : integer
    # @return an integer

    def recfn(self, A):
        z = 10**9+7
        if A == 1:
            return 1, 1
        if A == 0:
            return 0, 0
        x, y = self.recfn(A-1)
        ans = (x*2+y) % z
        return max(ans-(x+y), (x+y)) % z, min(ans-(x+y), (x+y)) % z

    def solve(self, A):
        a, b = self.recfn(A)
        return (a+b) % (10**9+7)


if __name__ == '__main__':
    A = 1250
    s = Solution()
    print(s.solve(A))
