class Solution:
    # @param A : list of integers
    # @return an integer
    def powmod(self, A,B,C):

        if A == 0 or A == 1:
            return A%C

        if B == 0:
            return 1

        sa = self.powmod(A,B//2,C)

        if B%2 == 0:
            return (sa*sa)%C
        else:
            return ((sa*sa)%C*A%C)%C
        
    def solve(self, A):
        mx = max(A) + 1
        prime = [True for _ in range(mx)]
        prime[1] = prime[0] = False

        i = 2
        while i*i<=mx:
            j = i*i
            while j<mx:
                if prime[j] == True:
                    prime[j] = False
                j += i
            i += 1

        ctr = 0
        ans = 1
        C = 1000000007
        for ele in A:
            if prime[ele]:
                ctr += 1
                ans = (ans*2)%C

        return  ans- 1
    

if __name__ == '__main__':
    s = Solution()
    print(s.solve([1,2,3,4,5]))
