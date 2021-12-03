from collections import OrderedDict

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        
        val_ind = dict()

        for ind,ele in enumerate(A):
            val_ind[ele] = ind

        sl = sorted(val_ind.keys())        

        prev_max_ind = 0

        for i in range(len(sl)-1,-1,-1):
            i = sl[i]
            val_ind[i] = max(val_ind[i], prev_max_ind)
            prev_max_ind = val_ind[i]

        ans = 0

        for i, ele in enumerate(A):
            j = val_ind[ele]
            ans = max(j-i,ans)

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maximumGap(A = [3, 5, 4, 2]))


