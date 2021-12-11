class Solution:
    # @param A : string
    # @return an integer
    def pos(self,chr,A):
        ctr = 0
        for ele in A:
            if ord(chr)>ord(ele):
                ctr += 1
        return ctr
                
    def findRankHelper(self, A):
        if len(A) == 1:
            return 1, 1, 0
        
        sa,prev,k = self.findRankHelper(A[1:])
        final_ans = (self.pos(A[0],A)*(prev*(k+1)) + sa)%1000003
        prev = (prev*(k+1))%1000003
        k+=1
        return final_ans,prev,k

    def findRank(self,A):
        return self.findRankHelper(A)[0]

if __name__ == '__main__':
    s = Solution()
    print(s.findRank("DTNGJPURFHY"))
