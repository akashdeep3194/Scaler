class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers

    def solve(self, A, B):
        pf_dict = dict()
        sm = 0
        i = 0
        ans = [-1]

        for index, ele in enumerate(A):

            sm += ele
            if sm == B:
                return A[0:index+1]
            elif pf_dict.get(sm-B, -1) == -1:
                pf_dict[sm] = index
            else:
                ans = A[pf_dict.get(sm-B)+1:index+1]
                break
        return ans


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    B = 5
    s = Solution()
    print(s.solve(A, B))
