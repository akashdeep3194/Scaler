from queue import Queue


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        visited = [[False for _ in range(len(A[0]))] for _ in range(len(A))]
        ctr = 0

        for i in range(len(A)):
            for j in range(len(A[0])):
                q = Queue()

                if A[i][j] == 1:
                    if not visited[i][j]:
                        q.put([i, j])
                        ctr += 1
                    else:
                        continue
                while not q.empty():

                    ele = q.get()
                    x = A[ele[0]][ele[1]]

                    if x == 0:
                        continue
                    if not visited[ele[0]][ele[1]]:
                        visited[ele[0]][ele[1]] = True

                        if ele[0]+1 < len(A):
                            q.put([ele[0]+1, ele[1]])
                        if ele[1]+1 < len(A[0]):
                            q.put([ele[0], ele[1]+1])
                        if ele[0]-1 >= 0:
                            q.put([ele[0]-1, ele[1]])
                        if ele[1]-1 >= 0:
                            q.put([ele[0], ele[1]-1])
                        if ele[0]+1 < len(A) and ele[1]+1 < len(A[0]):
                            q.put([ele[0]+1, ele[1]+1])
                        if ele[0]-1 >= 0 and ele[1]-1 >= 0:
                            q.put([ele[0]-1, ele[1]-1])
                        if ele[0]-1 >= 0 and ele[1]+1 < len(A[0]):
                            q.put([ele[0]-1, ele[1]+1])
                        if ele[0]+1 < len(A) and ele[1]-1 >= 0:
                            q.put([ele[0]+1, ele[1]-1])
        return ctr


if __name__ == '__main__':
    A = [
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1],
    ]
    s = Solution()
    print(s.solve(A))
