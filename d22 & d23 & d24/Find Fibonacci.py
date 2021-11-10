class Solution:
    # @param A : integer
    # @return an integer
    def findAthFibonacci(self, A):
        if A == 0 or A == 1:
            return A
        return self.findAthFibonacci(A-1)+self.findAthFibonacci(A-2)

# s = Solution()
# print(s.findAthFibonacci(5))
