class Solution:
    # @param A : tuple of integers
    # @return an integer
    def solve(self, A):
        a=A
        count = 0
        l = len(a)
        d = dict()
        for i in range(l):
            d[a[i]] = d.get(a[i],0) + 1
            if d[a[i]]>1:
                count+=1
        return count

