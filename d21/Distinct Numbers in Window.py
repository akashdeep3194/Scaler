class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        hm = dict()
        ans = []
        for ele in A[:B]:
            hm[ele] = hm.get(ele,0) + 1
        ans.append(len(hm.keys()))
        for i in range(1,len(A)-B+1):
            j = B+i-1
            hm[A[i-1]] -= 1
            if hm[A[i-1]] == 0:
                hm.pop(A[i-1])
            hm[A[i+B-1]] = hm.get(A[i+B-1],0) + 1
            x=hm.keys()
            ans.append(len(x))
        return ans

# s = Solution()
# A = [1, 2, 1, 3, 4, 3]
# B = 3
# print(s.dNums(A,B))
