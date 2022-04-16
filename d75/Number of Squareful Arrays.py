class Solution:
    # @param A : list of integers
    # @return an integer
    def __init__(self) -> None:
        self.ctr = 0

    def adj_sum(self, arr):
        for i in range(len(arr)-1):
            if int((arr[i]+arr[i-1])**0.5) == (arr[i]+arr[i-1])**0.5:
                continue
            else:
                return False
        else:
            return True

    def recfn(self, A, si, ans, li, is_ctr, a=None, b=None):
        if not is_ctr:
            return
        if si >= len(A):
            if li not in ans:
                if int((a+b)**0.5) == (a+b)**0.5 and is_ctr:
                    self.ctr += 1
                ans.append(li.copy())
            return
        for i in range(si, len(A)):
            A[si], A[i] = A[i], A[si]
            li.append(A[si])
            if a and b and is_ctr:
                is_ctr = (int((a+b)**0.5) == (a+b)**0.5)
            self.recfn(A, si+1, ans, li, is_ctr, b, A[si])
            li.pop()
            A[si], A[i] = A[i], A[si]

    def solve(self, A):
        A.sort()
        answer = []
        li = []
        if len(A) == 1:
            return self.ctr
        self.recfn(A, 0, answer, li, True)
        # for ans in answer:
        # print(ans)
        return self.ctr


if __name__ == '__main__':
    A = [1, 17, 8]
    s = Solution()
    print(s.solve(A))
