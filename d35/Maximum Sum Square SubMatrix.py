import sys

def maxsubarraysum(arr,size):
    
    sm = 0
    
    for i in range(size):
        sm += arr[i]

    ans = sm
    
    i = size

    while i<len(arr):
        sm = sm-arr[i-size] + arr[i]
        ans = max(sm,ans)
        i+=1
    
    return ans

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        n = len(A)
        m = len(A[0])

        pfarr = [[0 for _ in range(m)] for _ in range(n)]
        pfarr[0] = [A[0][i] for i in range(m)]


        for j in range(m):
            for i in range(1,n):
                pfarr[i][j] = A[i][j] + pfarr[i-1][j]


        ans = -10**10       

        for i in range(n):
            j=i
            while j<n:

                sm = 0
                
                size = j-i+1

                if size>B:
                    break

                if size!=B:
                    j += 1
                    continue
                else:
                    arr = []
                    for k in range(m):
                        arr.append(pfarr[j][k] - pfarr[i][k] + A[i][k])
                    sm = maxsubarraysum(arr,size)
                    ans = max(ans,sm)
                j+=1
        return ans

if __name__ == '__main__':
    
    s = Solution()
    A = [
    [-13, 70, 63, 1, 3, -77, 27],
    [-100, 69, -85, 65, -72, 43, 47],
    [-12, 43, -63, -91, -37, -51, -19],
    [88, 42, -92, -40, -79, 58, 54],
    [-12, 46, -10, 49, -57, -70, -80],
    [48, -33, 36, 83, -65, -74, 85],
    [-62, -47, -71, -76, 48, 23, 59]
    ]
    B = 7

    print(s.solve(A,B))
    smm = 0
    for ele in A:
        smm = smm + sum(ele)
    print(smm)
