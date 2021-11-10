class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        count = 0
        for i in range(len(A)-2):
            if A[i] == 'b':
                if A[i+1:i+3] == 'ob':
                    count += 1
        return count
# s = Solution()
# print(s.solve("bobkdfbobobsalfk"))
