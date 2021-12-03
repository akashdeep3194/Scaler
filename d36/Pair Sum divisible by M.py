class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        c = (10**9 + 7)
        for i,ele in enumerate(A):
            A[i]=ele%B
        s = dict()

        ans = 0

        for ele in A:
            if ele == 0:
                find = 0
            else:
                find = B-ele
            ans += s.get(find,0)
            ans = ans%c
            s[ele] = s.get(ele,0)+1         
        return ans%c

if __name__ == '__main__':
    A = [ 5, 17, 100, 11 ]
    B = 28
    s = Solution()
    print(s.solve(A,B))
