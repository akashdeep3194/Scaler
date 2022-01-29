from math import log10


class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        A = str(A)
        dc = dict()

        for i in range(len(A)):
            ele = 1
            for j in range(i, len(A)):
                k = int(A[j])
                ele = ele*k
                dc[ele] = dc.get(ele, 0) + 1
                if dc[ele] == 2:
                    return 0
        return 1


if __name__ == "__main__":
    s = Solution()
    print(s.colorful(A=236))
