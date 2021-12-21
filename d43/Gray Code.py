class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        if A == 1:
            return [0,1]
        si = A-1
        sa = self.grayCode(si)
        ans = []
        ans.extend(sa)
        for i in range(len(sa)-1,-1,-1):
            ans.append(sa[i]+2**(A-1))
        return ans
    
if __name__ == '__main__':
    s = Solution()
    print(s.grayCode(3))
