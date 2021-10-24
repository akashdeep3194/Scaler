class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        d = dict()
        dist = len(A)+1

        for i,ele in enumerate(A):
            if d.get(ele,0) != 0:
                si  = d[ele][1]
            d[ele] = [d.get(ele,[0,-1])[0]+1,i]

            if d.get(ele,0)[0]>1:
                ei = i
                dist  = min(dist,ei-si)
        if dist == len(A)+1:
            return -1
        else:
            return dist

# s = Solution()
# A = [1, 1]
# print(s.solve(A))
