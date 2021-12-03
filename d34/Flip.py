class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        A = "1" + A
        n = len(A)
        pf = [0 for _ in range(n)]
        if A[0] == '1':
            pf[0] = -1
        else:
            pf[0] = 1
            
        for i in range(1,n):
            ele = A[i]
            if ele == '1':
                pf[i] = pf[i-1] - 1
            else:
                pf[i] = pf[i-1] + 1
        mn = mx = pf[0]
        ans = mni = mxi = 0
        ans_arr = [-1,-1]

        rmax = [0 for _ in range(len(pf))]
        rmax[-1] = (pf[-1],len(pf)-1)
        for i in range(len(pf)-2,-1,-1):
            if rmax[i+1][0] <= pf[i]:
                rmax[i] = (pf[i],i)
            else:
                rmax[i] = rmax[i+1]
        for i, ele in enumerate(pf):

            if ele < mn:
                mni = i
                mn = ele
            mx = rmax[i][0]
            mxi = rmax[i][1]

            if mx - mn>ans:
                if mni == 0 and A[0] == '0':
                    ans_arr[0] = mni + 1 - 1
                else:
                    ans_arr[0] = mni + 2 - 1
                ans_arr[1] = mxi + 1 - 1
                ans = mx - mn

        if ans == 0 and A[0] == '1':
            return []
        elif ans == 0 and A[0] == '0':
            return [1, 1]
        else:
            return ans_arr

# s = Solution()
# print(s.flip("110100100011111000000"))
