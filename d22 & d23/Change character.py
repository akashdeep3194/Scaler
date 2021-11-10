class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        arr = [0 for _ in range(26)]
        count = 0
        for i,ele in enumerate(A):
            if (arr[ord(ele)-97]) == 0:
                count += 1
            arr[ord(ele)-97] += 1
        arr = sorted(arr)
        for i,ele in enumerate(arr):
            B = B - ele
            if B>=0 and ele>0:
                count -= 1
            elif B<0:
                return count
        return count

# s = Solution()
# print(s.solve("aabbdhdhabdx",3))
