class Solution:
    # @param A : integer
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        
        dc = dict()

        for ele in B:
            dc[ele] = dc.get(ele,0) + 1
        for k,v in dc.items():
            if v%A != 0:
                return -1
        return 1
        