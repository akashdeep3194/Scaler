
class Solution:
    # @param A : list of integers
    # @return an integer
    def isPrime(self,ele):
        if ele <2:
            return False
        i=2
        while i*i<=ele:
            if ele%i == 0:
                return False
            i+=1
        return True

    def solve(self, A):
        count = 0
        for ele in A:
            if self.isPrime(ele):
                count+=1
        return count

s = Solution()
print(s.solve([-11, 7, 8, 9, 10, 11]))
