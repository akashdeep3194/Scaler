from math import log2
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        ans = 0
        mx = int(log2(max(A))) + 1
        for i in range(mx):
            ctr = 0
            for ele in A:
                if ele&(1<<i):
                    ctr += 1
            if ctr%3 != 0:
                ans += 1<<i
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber((6,2,16,2,2,6,6)))
