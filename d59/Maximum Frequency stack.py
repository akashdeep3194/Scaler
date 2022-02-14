class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        arr = []
        freq = dict()
        max_freq_ele = []
        max_freq = 0
        res = []
        for ele in A:
            if ele[0] == 1:
                ele = ele[1]
                arr.append(ele)
                res.append(-1)
                freq[ele] = freq.get(ele, 0) + 1
                if max_freq <= freq[ele]:
                    max_freq_ele.append(ele)
                    max_freq = freq[ele]
                    prev_ele = ele
                else:
                    max_freq_ele.append(prev_ele)
            else:
                x = max_freq_ele.pop()
                if freq[arr[-1]] >= freq[x]:
                    freq[arr[-1]] = freq[arr[-1]]-1
                    res.append(arr.pop())

                else:
                    arr.remove(x)
                    freq[x] = freq[x]-1
                    res.append(x)
        return res


if __name__ == "__main__":
    s = Solution()
    A = [
        [1, 5],
        [1, 7],
        [1, 5],
        [1, 7],
        [1, 4],
        [1, 5],
        [2, 0],
        [2, 0],
        [2, 0],
        [2, 0]]
    print(s.solve(A))
