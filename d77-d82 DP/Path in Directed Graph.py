from queue import Queue
from re import L

from numpy import empty


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        graph = []
        for _ in range(A+1):
            graph.append([])

        for ele in B:
            graph[ele[0]].append(ele[1])

        q = Queue()

        visited = [False for _ in range(A+1)]

        q.put(1)
        visited[1] = True

        while not (q.empty()):
            x = q.get()
            if x == A:
                return 1
            for ele in graph[x]:
                if visited[ele]:
                    continue
                if ele == A:
                    return 1
                visited[ele] = True
                q.put(ele)
        return 0


if __name__ == '__main__':
    A = 5
    # B = [[1, 2],
    #      [2, 3],
    #      [3, 4],
    #      [4, 5],
    #      [1, 3]]
    B = [[1, 2],
         [2, 3],
         [3, 4],
         [4, 5]]

    s = Solution()
    print(s.solve(A, B))
