class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        sm = 0
        pf_arr = []
        dc = dict()
        ans = []
        for i in range(len(A)):
            sm += A[i]
            if sm == 0 and len(ans) < i+1:
                ans = A[:i+1]
            pf_arr.append(sm)
            if len(dc.get(pf_arr[i], [])) == 2:
                dc[pf_arr[i]][1] = i
                if dc[pf_arr[i]][1]-dc[pf_arr[i]][0] > len(ans):
                    ans = A[dc[pf_arr[i]][0]+1:dc[pf_arr[i]][1]+1]
            else:
                arr = dc.get(pf_arr[i], [])
                arr.append(i)
                dc[pf_arr[i]] = arr
                if len(dc.get(pf_arr[i], [])) == 2:
                    dc[pf_arr[i]][1] = i
                    if dc[pf_arr[i]][1]-dc[pf_arr[i]][0] > len(ans):
                        ans = A[dc[pf_arr[i]][0]+1:dc[pf_arr[i]][1]+1]

        return ans


if __name__ == "__main__":
    s = Solution()
    A = [1, 2, -1, 1, 3, -1, 1, 4]
    print(s.lszero(A))
