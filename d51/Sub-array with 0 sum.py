class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        pf_arr = []
        sm = 0
        dc = dict()
        for i in range(len(A)):
            sm += A[i]
            pf_arr.append(sm)
            dc[sm] = dc.get(sm, 0) + 1
            if dc[sm] > 1 or sm == 0:
                return 1
        return 0
