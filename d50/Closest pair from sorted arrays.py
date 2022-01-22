class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers

    def solve(self, A, B, C):
        answer = [A[0], B[0]]
        ans = abs(A[0]+B[0]-C)
        ai = len(A)
        aj = len(B)
        i = 0
        j = len(B) - 1
        while i < len(A) and j >= 0:
            if A[i] + B[j] == C:
                return [A[i], B[j]]
            if A[i] + B[j] > C:
                if ans > abs(A[i]+B[j]-C):
                    answer = [A[i], B[j]]
                    ai = i
                    aj = j
                    ans = abs(A[i]+B[j]-C)

                if ans == abs(A[i]+B[j]-C):
                    if ai > i:
                        answer = [A[i], B[j]]
                        ai = i
                        aj = j
                    elif ai == i:
                        if aj > j:
                            answer = [A[i], B[j]]
                            ai = i
                            aj = j

                j -= 1
            if A[i] + B[j] < C:
                if ans > abs(A[i]+B[j]-C):
                    answer = [A[i], B[j]]
                    ai = i
                    aj = j
                    ans = abs(A[i]+B[j]-C)

                if ans == abs(A[i]+B[j]-C):
                    if ai > i:
                        answer = [A[i], B[j]]
                        ai = i
                        aj = j
                    elif ai == i:
                        if aj > j:
                            answer = [A[i], B[j]]
                            ai = i
                            aj = j

                i += 1

        return answer


if __name__ == "__main__":
    s = Solution()
    A = [5, 10, 20]
    B = [1, 2, 30]
    C = 13
    print(s.solve(A, B, C))
