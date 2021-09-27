class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        right_max = [0 for ele in range(len(A))]
        max_num = A[-1]
        j=0
        for i in range(len(A)-1,-1,-1):
            right_max[-1*j-1] = max(A[i],max_num)
            max_num = right_max[-1*j-1]
            j+=1
        ans = []
        for ind,ele in enumerate(A):
            if ind == len(A)-1:
                ans.append(ele)
            elif ele>right_max[ind+1] and ind+1<len(A):
                ans.append(ele)
        return ans

s = Solution()
print(s.solve([1,21,3,4,5,7,5,8,5,-2,9,7,0]))