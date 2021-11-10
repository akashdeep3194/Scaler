class Solution:
    # @param A : integer
    # @return a list of list of integers
    def towerOfHanoi(self, A):
        return self.TOH(A,1,3,2)

    def TOH(self,N,A,B,C):
        if N==1:
            return [[1,A,B]]
        else:
            sa1 = self.TOH(N-1,A,C,B)
            li = [N,A,B]
            sa1.append(li)
            sa2 = self.TOH(N-1,C,B,A)
            sa1.extend(sa2)
        return sa1

s = Solution()
print(s.towerOfHanoi(3))
