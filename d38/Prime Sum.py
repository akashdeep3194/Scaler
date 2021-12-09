class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        num = A+1
        arr = [True for i in range(num)]
        i = 2
        
        while i*i<=num:
            if arr[i] == True:
                j = i*i
                while j<num:
                    arr[j] = False
                    j += i
            i += 1            

        for i in range(2,num):
            if arr[i] == True:
                if arr[A-i] == True:
                    return [i,A-i]
            else:
                continue
        return

if __name__ == '__main__':
    s = Solution()
    print(s.primesum(200))
