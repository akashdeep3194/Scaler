class Solution:
    # @param A : list of integers
    # @return an integer
    def candy(self, A):
        candies = 1
        candy = 1
        arr = [1]
        for i in range(len(A)-1):
            if A[i] < A[i+1]:
                candy += 1
            else:
                candy = 1
            candies += candy
            arr.append(candy)
        for i in range(len(A)-1, 0, -1):
            if A[i-1] > A[i] and arr[i-1] <= arr[i]:
                candy = arr[i]-arr[i-1] + 1
            else:
                candy = 0
            candies += candy
            arr[i-1] += candy
        return candies


s = Solution()
print(s.candy(A=[1, 5, 2, 1]))
# 1 3 2 1
# 1 2 1 1
