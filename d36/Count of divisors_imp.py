class Solution:
    # @param A : list of integers
    # @return a list of integers
    def SmallestPrimeFactor(self,x):
        i = 2
        if x==2:
            return 2
        while i*i<=x:
            if x%i == 0:
                return i
            i+=1
        return x
            

    def solve(self, A):
        
        mx = max(A)

        factors=[1 for _ in range(mx+1)]

        for i in range(2, mx+1):
            j = i

            while j<mx+1:
                factors[j]+=1
                j+=i
        
        ans = []
        
        for ele in A:
            ans_sa = factors[ele]                                    
            ans.append(ans_sa)
        return ans

if __name__ == '__main__':
    s = Solution()
    A = [55]
    print(s.solve(A))
