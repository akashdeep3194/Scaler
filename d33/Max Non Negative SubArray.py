class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        m_arr = []
        m_sum = 0
        curr_arr = []
        c_sum = 0
        for ele in A:
            if ele <0:
                if c_sum>=m_sum:
                    if c_sum == m_sum and len(curr_arr)<len(m_arr):
                        continue
                    m_arr = curr_arr
                    m_sum = c_sum
                c_sum = 0
                curr_arr = []
                continue
            curr_arr.append(ele)
            c_sum+=ele
        if m_sum>c_sum:
            return m_arr
        else:
            if m_sum==c_sum and len(m_arr)>=len(curr_arr):
                return m_arr
            else:
                return curr_arr
                
# s = Solution()
# A = [1, 2, 5, -7, 2, 3]
# print(s.maxset(A))
