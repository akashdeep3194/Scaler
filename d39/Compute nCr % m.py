class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        ans = 1
        arr1 = [0 for _ in range(B+1)]    
        arr1[0] = arr1[1] = 1
        arr2 = [0 for _ in range(B+1)]    
        arr2[0] = arr2[1] = 1
        n = 2

        while n<=A:
            for i in range(1,min(B+1,n+1)):
                arr2[i] = (arr1[i] + arr1[i-1])%C
                if n == A and i == B:
                    return arr2[i]
            n += 1
            arr1,arr2 = arr2,arr1

        return arr1[B]
        
if __name__ == '__main__':
    s = Solution()
    print(s.solve(30,24,56))
