from functools import cmp_to_key

class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    # def comp(self,c,d):
    #     for i in range(min(len(c[0]),len(d[0]))):
    #         if c[1][c[0][i]]>c[1][d[0][i]]:
    #             return 1
    #         elif c[1][c[0][i]]<c[1][d[0][i]]:
    #             return -1
    #         else:
    #             continue
    #     if len(c[0])<len(d[0]):
    #         return 1
    #     else:
    #         return -1
    def check(self,ele,elem,hm):
        for j in range(min(len(ele),len(elem))):
            if hm[ele[j]] > hm[elem[j]]:
                return 0
            elif ele[j] == elem[j]:
                continue
            else:
                return 1
        if len(ele) > len(elem):
            return 0
        return 1

    def solve(self, A, B):
        hm = dict()
        for ind, ele in enumerate(B):
            hm[ele] = ind
   
        x = []
        n = len(A)

        for i, ele in enumerate(A[:n-1]):

            if self.check(ele,A[i+1],hm) == 0:
                return 0
            else:
                continue
        return 1

# s = Solution()
# A = [ "zhello", "scaler", "interviewbit" ]
# B = "adzhbcfegskjlponmirqtxwuvy"
# print(s.solve(A,B))
