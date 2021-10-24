class Solution:
    # @param A : list of integers
	# @return a list of integers
    def lszero(self, A):
        pf = []
        freq = dict()
        sum = dist = 0
        si = -1
        ei = -1
        for ind,ele in enumerate(A):
            sum += ele
            pf.append(sum)
            
            if sum == 0:
                si = -1
                dist = ind+1
                ei = ind
            if freq.get(sum,0) == 0:
                freq[sum] = [freq.get(sum,0)+1,ind,-1]
            else:
                freq[sum][0] = freq[sum][0]+1
                freq[sum][2] = ind
                if dist < ind-freq[sum][1]:
                    dist = ind-freq[sum][1]
                    si = freq[sum][1]
                    ei = ind
        return A[si+1:ei+1]

# A = [1,2,-2,4,-4]
# s = Solution()
# print(s.lszero(A))
