from math import gcd

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        lcm = max(A)

        pf = [[0,[]] for _ in range(lcm+1)]
        pf[1] = [1,[]]

        i = 2

        while i<(lcm+1):        
            if pf[i][0] == 0:
                pf[i][1].append(i)
                j = i*2
                while j<lcm+1:
                    pf[j][0] += 1
                    pf[j][1].append(i)
                    j += i
            i += 1

        s = set()

        for ele in A:
            for el in pf[ele][1]:
                s.add(el)
        return len(s)
    
if __name__ == '__main__':
    s = Solution()
    print(s.solve([1, 6]))
