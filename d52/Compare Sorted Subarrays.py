class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def powmod(self, a, b, p=10**9+7):
        if a == 1:
            return 1
        if b == 1:
            return a % p
        res = 1
        while b > 1:
            if b & 1 != 0:
                res = (res*a) % p
            a = (a*a) % p
            b = b//2
        res = (res*a) % p
        return res % p

        x = self.powmod(a, b//2)
        if b & 1 == 0:
            return (x*x) % p
        else:
            return ((a*x) % p*x) % p

    def solve(self, A, B):
        res = []
        pf = []
        sm = 0
        for ele in A:
            sm += self.powmod(2, ele)
            pf.append(sm)

        for ele in B:
            l1 = ele[0]
            r1 = ele[1]
            l2 = ele[2]
            r2 = ele[3]

            if r2-l2 != r1-l1:
                res.append(0)
                continue
            num1 = pf[r1]-pf[l1] + self.powmod(2, A[l1])
            num2 = pf[r2]-pf[l2] + self.powmod(2, A[l2])

            if num1 == num2:
                res.append(1)
            else:
                res.append(0)
        return res


if __name__ == "__main__":
    s = Solution()
    A = [1, 7, 11, 8, 11, 7, 1]
    B = [
        [0, 2, 4, 6]
    ]
    # print(s.powmod(2, 7))
    print(s.solve(A, B))
    # print(s.DictEquals(d1, d2))
