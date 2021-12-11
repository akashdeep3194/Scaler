class Solution:
    # @param A : string
    # @return an integer
    def invmod(self,num,C):
        res = 1
        p = C-2
        while p>0:
            if p&1 != 0:
                res = (res * num)%C
            num = (num*num)%C
            p = p//2
            
        return res%C
            
            
    def pos(self,chr,A):
        ctr = 0
        for ele in A:
            if ord(chr)>ord(ele):
                ctr += 1
        return ctr
                
    def findRankHelper(self, A):
        if len(A) == 1:
            return 1, 1, 0,{A:1},1

        sa,prev,k,dc,dv = self.findRankHelper(A[1:])
        dc[A[0]] = dc.get(A[0],0) + 1

        if dc[A[0]] > 1:
            dv = dv*dc[A[0]]
        prev = (prev*(k+1))%1000003            
        num = ((self.pos(A[0],A)*prev)%1000003)        
        inv_den = self.invmod(dv,1000003)
        final_ans = ((num*inv_den)%1000003 + sa)%1000003
        k+=1

        return final_ans,prev,k,dc,dv

    def findRank(self,A):
        return int(self.findRankHelper(A)[0])%1000003

if __name__ == '__main__':
    s = Solution()
    print(s.findRank("bbbcccaaa"))
