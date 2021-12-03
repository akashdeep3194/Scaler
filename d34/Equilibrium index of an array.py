class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        ts = sum(A)
        ls = 0

        for i,ele in enumerate(A):
            rs = ts - ls - ele
            if ls == rs:
                return i
            ls += ele
        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.solve([-7, 1, 5, 2, -4, 3, 0]))
