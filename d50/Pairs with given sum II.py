class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        z = 10**9+7

        i = 0
        j = len(A) - 1
        count = 0
        l = 1
        r = 1

        while i <= j:
            if A[i] + A[j] == B:
                if A[i] == A[j]:
                    count += int((j-i+1)*(j-i)//2)
                    return count % z
                while i <= j and i < len(A)-1:
                    if A[i+1] == A[i]:
                        l += 1
                        i += 1
                    else:
                        break
                while i <= j and j > 0:
                    if A[j] == A[j-1]:
                        r += 1
                        j -= 1
                    else:
                        break
                count = (count + l*r) % z
                l = 1
                r = 1
                i += 1
                j -= 1

            elif A[i]+A[j] > B:
                j -= 1

            elif A[i]+A[j] < B:
                i += 1
        return count


if __name__ == "__main__":
    s = Solution()
    A = [1, 2, 2, 2, 3, 4, 5, 5, 6, 6, 6, 6]
    B = 8
    print(s.solve(A, B))
