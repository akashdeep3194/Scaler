class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        a=A
        a = sorted(a)
        l = len(a)
        for i in range(l-1):
            if a[i+1] - a[i] == 1:
                continue
            else:
                return 0
        return 1
    
    def solve_alt(self, A):
        a=A
        mn = mx = a[0]

        dictionary = dict()
        for ele in A:
            dictionary[ele] = dictionary.get(ele,0) + 1
            if ele < mn:
                mn = ele
            if ele>mx:
                mx = ele

        for ele in range(mn,mx+1):
            if dictionary.get(ele,0) == 0:
                return 0
        return 1


s = Solution()
print(s.solve_alt([1,2,3,9,8,7,5,4]))

