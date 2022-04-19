class Solution:
    # @param A : integer
    # @return an integer

    def recfn(self, A):

        for i in range(1, 7):
            sm += self.recfn(A-i)

    def solve(self, A):
