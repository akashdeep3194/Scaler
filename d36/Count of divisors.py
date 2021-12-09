class Solution:
    # @param A : list of integers
    # @return a list of integers

    def solve(self, A):
        
        mx = max(A)

        spf = [-1 for _ in range(mx+1)]
        i = 2

        while i*i<=mx:

            if spf[i] == -1:
                spf[i] = i
            
            if spf[i] == i:
                k = i*i
                while k<=mx:
                    if spf[k] == -1:
                        spf[k] = i
                    k += i

            i+=1

        
        ans = []
        
        for ele in A:
            i=2
            ans_sa = 1
            ele_cpy = ele


            while ele_cpy != 1:

                ctr = 0
                fct = spf[ele_cpy]

                if fct == -1:
                    ele_cpy = ele_cpy//ele_cpy
                    ctr += 1

                else:
                    while ele_cpy%fct == 0:
                        ele_cpy = ele_cpy//fct
                        ctr += 1
                    
                ans_sa = ans_sa*(ctr+1)                                    

            ans.append(ans_sa)
        return ans

if __name__ == '__main__':
    s = Solution()
    A = [168]
    print(s.solve(A))
