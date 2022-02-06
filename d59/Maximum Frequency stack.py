class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        arr = []
        freq = dict()
        max_freq_ele = []
        max_freq = 0
        for ele in A:

            ele = A[1]

            arr.append(ele)
            freq[ele] = freq.get(ele, 0)+1
            if freq[ele] >= max_freq:
                max_freq_ele.append(ele)
            else:
                max_freq_ele.append()

            arr.remove
