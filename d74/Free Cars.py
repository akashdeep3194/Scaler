import heapq


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        x = list(zip(A, B))
        x.sort()
        profit = 0
        prev_time = 0
        heap = []
        heapq.heapify(heap)
        for ele in x:
            if ele[0] > prev_time:
                heapq.heappush(heap, ele[1])
                profit = (profit + ele[1]) % (10**9+7)
                prev_time += 1
            else:
                if ele[1] > heap[0]:
                    profit = (profit - heapq.heappop(heap)) % (10**9+7)
                    profit = (profit + ele[1]) % (10**9+7)
                    heapq.heappush(heap, ele[1])
        return profit


# s = Solution()
# A = [6, 8, 6, 8, 3, 3, 6, 4, 5, 3, 8, 4, 8]
# B = [9, 7, 5, 11, 8, 12, 4, 5, 7, 7, 12, 4, 2]
# print(s.solve(A, B))
