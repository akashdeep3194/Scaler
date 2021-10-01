class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        arr = [0 for _ in range(A)]
        for ele in B:
            start = ele[0]-1
            end = ele[1]-1
            amt = ele[2]

            arr[start] += amt
            if end+1<A:
                arr[end+1] += -1*amt
        for i in range(A-1):
            arr[i+1]=arr[i]+arr[i+1]
        return arr

# s = Solution()
# print(s.solve(5,[[1, 2, 10], [2, 3, 20], [2, 5, 25]]))

