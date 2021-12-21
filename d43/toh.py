class Solution:
    # @param A : integer
    # @return a list of list of integers

    def toh(self,start,stop,aux,N):
        if N == 1:
            return [[N,start,stop]]

        arr1 = self.toh(start,aux,stop,N-1)
        arr1.append([N,start,stop])
        arr1.extend(self.toh(aux,stop,start,N-1))
        
        return arr1
        
        
    def towerOfHanoi(self, A):
        return self.toh(1,3,2,A)
if __name__ == '__main__':
    s = Solution()
    print(s.towerOfHanoi(3))
