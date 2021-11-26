class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def sortStr(self,ele,count=[]):
        if len(count) == 0:
            count = [0 for _ in range(26)]

            for char in ele:
                count[ord(char)-97] += 1
        ans = ""

        for ind,ctr in enumerate(count):
            ans = ans + chr(ind+97)*ctr
        return ans
    
    def isPerm(self,s1,s2,count):
        if self.sortStr(s1,count) == s2:
            return True
        else:
            return False
        
    def solve(self, A, B):
        if len(A)>len(B):
            return 0
        n = len(A)
        A = "".join(sorted(A))
        ctr = 0

        count = [0 for _ in range(26)]

        for char in B[0:n]:
            count[ord(char)-97] += 1

        for i in range(0,len(B)-n+1):
            if self.isPerm(B[i:n+i],A,count):
                ctr += 1
            count[ord(B[i])-97] -= 1

            if n+i<len(B):
                count[ord(B[n+i])-97] += 1 
        return ctr

# s = Solution()
# A = "asdf"
# B = "asdfasdf"
# print(s.solve(A,B))
