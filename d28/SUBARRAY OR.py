class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        sum = 0
        n = len(A)
        t = int(n*(n+1)/2)
        # checking for 27 bits
        for i in range(27):
            sum_bit = 0
            # checking each element's ith bit 
            cont_zeros = 0
            for j,ele in enumerate(A):

                # if element's ith bit is set
                if ele & 2**i == 0:
                    cont_zeros += 1
                else:
                    sum_bit += cont_zeros*(cont_zeros+1)/2
                    cont_zeros = 0

            sum_bit += cont_zeros*(cont_zeros+1)/2                        
            sum_bit = t - sum_bit

            sum = sum + (sum_bit*2**i)%10000000070
        return int(sum%1000000007)

# s = Solution()

# print(s.solve([1,2,3]))
