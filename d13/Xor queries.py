class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        pf = []
        ctr = 0

        ans = []


        for ele in A:
            if ele == 1:
                ctr += 1
            pf.append(ctr)
        for ele in B:
            l = ele[0]-1
            r = ele[1]-1
            ones_ct = pf[r] - pf[l] + A[l]
            zeros_ct = r-l+1 - ones_ct
            ans.append([ones_ct%2,zeros_ct])
        
        return ans


# A=[1,0,0,0,1]
# B=[ [2,4],
#     [1,5],
#     [3,5] ]
# s = Solution()
# print(s.solve(A,B))

