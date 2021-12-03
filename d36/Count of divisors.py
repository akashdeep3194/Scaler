class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        ans = []
        for ele in A:
            dc = dict()

            i=2
            ans_sa = 1

            while i*i<=ele:
                if ele%i == 0:
                    dc[i] = dc.get(i,0) + 1
                    ele = ele//i
                else:
                    ans_sa *= (dc.get(i,0) + 1)
                    if dc.get(i,0) > 0:
                        dc.pop(i)
                    i+=1
                    
            if ele != 1:
                dc[ele] = dc.get(ele,0) + 1
            for k,v in dc.items():
                ans_sa *= (v + 1)
                
            ans.append(ans_sa)
        return ans
if __name__ == '__main__':
    s = Solution()
    A = [8, 9, 10,121,168]
    print(s.solve(A))
