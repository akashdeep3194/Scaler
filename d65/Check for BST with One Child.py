class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        range_ele = [-10**9, 10**9]
        prev = A[0]
        for ele in A[1:]:
            if ele < prev:
                if ele > range_ele[0] and ele < range_ele[1]:
                    range_ele[0] = range_ele[0]
                    range_ele[1] = min(prev, range_ele[1])
                else:
                    return "NO"
            else:
                if ele > range_ele[0] and ele < range_ele[1]:
                    range_ele[0] = max(prev, range_ele[0])
                    range_ele[1] = range_ele[1]
                else:
                    return "NO"
            prev = ele
        return "YES"


if __name__ == "__main__":
    s = Solution()
    print(s.solve([1, 5, 6, 4]))
