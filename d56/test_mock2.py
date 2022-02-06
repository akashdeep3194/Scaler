class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):
        dc = dict()

        for i in range(len(A)):
            for j in range(i+1, len(A)):
                sm = A[i]+A[j]
                arr = dc.get(sm, [])
                arr.append((i, j))
                dc[sm] = arr

        for i in range(len(A)):
            for j in range(i+1, len(A)):
                sm = A[i]+A[j]
                arr = dc.get(sm)
                if len(arr) > 1:
                    ans = [i, j, arr[1][0], arr[1][1]]
                    return ans
        return []


if __name__ == "__main__":
    s = Solution()
    print(s.equal([3, 4, 7, 1, 2, 9, 8]))
