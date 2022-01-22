class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def isWorkersCountlteK(self, arr, time, k, B):
        sm = 0
        workers = 1
        for i in range(len(arr)):
            if sm + arr[i]*B <= time:
                sm += arr[i]*B
            else:
                workers += 1
                sm = arr[i]*B
                if workers > k:
                    return False
        return True

    def paint(self, A, B, C):
        sm = 0
        for ele in C:
            sm += ele
        max_time = sm
        min_time = max(C)

        while min_time <= max_time:
            mid = (min_time+max_time)//2
            if self.isWorkersCountlteK(C, mid*B, A, B):
                ans = mid
                max_time = mid - 1
            else:
                min_time = mid + 1
        return (ans*B) % 10000003


if __name__ == '__main__':
    A = 3
    B = 10
    C = [185, 186, 938, 558, 655, 461, 441, 234, 902, 681]
    s = Solution()
    print(s.paint(A, B, C))
