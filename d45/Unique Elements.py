class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        s = set()
        prev = A[0]
        count = 0
        s.add(prev)

        for i in range(1,len(A)):
            ele = A[i]
            if ele in s:
                A[i] = prev + 1
                count += A[i] - ele
            prev = A[i]
            s.add(prev)
        return count

if __name__ == '__main__':
    s = Solution()
    print(s.solve([4, 2, 5, 3, 3]))

