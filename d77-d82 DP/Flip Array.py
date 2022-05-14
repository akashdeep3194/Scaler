class Solution:
    # @param A : tuple of integers
    # @return an integer
    def __init__(self) -> None:
        self.ans = 10**9
        self.ctr = 10**9

    def solve(self, A):
        # self.solveH(A)
        return self.solveR(A)[1]
        # return self.ctr

    def solveH(self, A, i=0, s=0, ctr=0):
        if i == len(A):
            if s >= 0:
                if self.ans >= s:
                    if self.ans == s:
                        self.ctr = min(ctr, self.ctr)
                    else:
                        self.ctr = ctr
                    self.ans = s
            return

        self.solveH(A, i+1, s=s+A[i]*-1, ctr=ctr+1)
        self.solveH(A, i+1, s=s+A[i], ctr=ctr)

    def solveR(self, A, i=0, closest_gt=0, dp=None):
        if not dp:
            sm = 0
            for ele in A:
                if ele < 0:
                    ele = ele*-1
                sm += ele
            dp = [[-1 for _ in range(-1*sm, sm)] for _ in range(len(A)+1)]

        if i == len(A):
            return 0, 0
        if dp[i+1][closest_gt+A[i]] == -1:
            dp[i+1][closest_gt+A[i]] = self.solveR(A, i+1, closest_gt+A[i], dp)
        smx, x = dp[i+1][closest_gt+A[i]]

        if dp[i+1][closest_gt-A[i]] == -1:
            dp[i+1][closest_gt-A[i]] = self.solveR(A, i+1, closest_gt-A[i], dp)
        smy, y = dp[i+1][closest_gt-A[i]]

        my = smy + A[i]
        mx = smx - A[i]

        if smx < closest_gt+A[i]:
            return my, y
        elif smy < closest_gt-A[i]:
            return mx, x+1

        if my < mx:
            return my, y
        elif my > mx:
            return mx, x+1
        else:
            return (mx+my)//2, min(x+1, y)


if __name__ == '__main__':
    A = [8, 4, 5, 7, 6, 2]
    s = Solution()
    print(s.solve(A))
