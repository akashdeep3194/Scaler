from math import gcd


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        sld = dict()
        maxl = 0
        ans = 0
        sm = 0
        for i in range(len(A)):
            dc = dict()
            maxl = 0
            arr = []
            val = 1
            for j in range(i+1, len(A)):
                sm += 1
                if A[i] == A[j] and B[i] == B[j]:
                    val += 1
                elif A[j] == A[i]:
                    slope = "1.0/0.0"
                    arr = dc.get(slope, [])
                    arr.append((A[j], B[j],))
                    dc[slope] = arr
                elif B[j] == B[i]:
                    slope = "0.0/1.0"
                    arr = dc.get(slope, [])
                    arr.append((A[j], B[j],))
                    dc[slope] = arr
                elif A[j] > A[i]:
                    num = (B[j] - B[i])
                    den = (A[j] - A[i])
                    gcd_val = gcd(num, den)
                    slope = str(num/gcd_val) + "/" + str(den/gcd_val)
                    arr = dc.get(slope, [])
                    arr.append((A[j], B[j],))
                    dc[slope] = arr
                else:
                    num = (B[i]-B[j])
                    den = (A[i]-A[j])
                    gcd_val = gcd(num, den)
                    slope = str(num/gcd_val) + "/" + str(den/gcd_val)
                    arr = dc.get(slope, [])
                    arr.append((A[j], B[j],))
                    dc[slope] = arr
                if len(arr) > maxl:
                    maxl = len(arr)
            maxl = maxl + val
            ans = max(maxl, ans)
        return ans


if __name__ == "__main__":
    s = Solution()
    A = [0, 0, 0, 1, 2, 0]
    B = [0, 1, 2, 1, 2, 0]
    print(s.solve(A, B))
