class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        ws = 0

        for i,ele in enumerate(A):
            if ele<=B:
                ws += 1
        ctr = 0

        for i in range(ws):
            if A[i] <= B:
                ctr += 1


        i = 1
        j = i + ws - 1
        ans = ctr

        while j<len(A):
            if A[i-1]<=B:
                ctr -= 1
            if A[j]<=B:
                ctr += 1

            ans = max(ctr,ans)

            j += 1
            i += 1
        return ws - ans

if __name__ == '__main__':

    A = [ 52, 7, 93, 47, 68, 26, 51, 44, 5, 41, 88, 19, 78, 38, 17, 13, 24, 74, 92, 5, 84, 27, 48, 49, 37, 59, 3, 56, 79, 26, 55, 60, 16, 83, 63, 40, 55, 9, 96, 29, 7, 22, 27, 74, 78, 38, 11, 65, 29, 52, 36, 21, 94, 46, 52, 47, 87, 33, 87, 70 ]
    B = 19

    s = Solution()
    print(s.solve(A,B))
