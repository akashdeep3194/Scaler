class Solution:
    # @param A : list of integers
    # @return an integer
    def cntBits(self, A):
        n = len(A)
        ans = 0
        for bit in range(32):
            ones = 0
            for ele in A:
                if ele&1<<bit:
                    ones += 1
            zeros = n-ones
            ans = (ans + (zeros*ones)%(10**9+7))%(10**9+7)
        
        return (ans*2)%(10**9+7)
    
if __name__ == '__main__':
    s = Solution()
    print(s.cntBits([1,2,3]))

