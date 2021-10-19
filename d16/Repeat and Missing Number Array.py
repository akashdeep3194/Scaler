class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        sum = 0
        x = 0
        c = 1
        grp1 = grp2 = 0

        for ele in A:
            sum += ele
            x = x^ele^c
            c+=1
        ctr = 0
        while(x>0):
            if x&1 == 1:
                break
            x = x>>1
            ctr+=1

        ctr = 2**ctr
        c = 1
        for ele in A:
            if ele&ctr == ctr:
                grp1 = grp1^ele
            else:
                grp2 = grp2^ele
            if c&ctr == ctr:
                grp1 = grp1^c
            else:
                grp2 = grp2^c
            c+=1

        expected_sum = len(A)*(len(A)+1)/2

        if expected_sum - grp1 + grp2 == sum:
            return [grp2,grp1]
        else:
            return [grp1,grp2]

s = Solution()
print(s.repeatedNumber([4, 1, 2, 5, 1]))
