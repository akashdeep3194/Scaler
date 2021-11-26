class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def sortStr(self,ele):
        count = [0 for _ in range(26)]
        ans = ""
        for char in ele:
            count[ord(char)-97] += 1
        for ind,ctr in enumerate(count):
            ans = ans + chr(ind+97)*ctr
        return ans

    def anagrams(self, A):
        A = list(A)
        for ind, ele in enumerate(A):
            ele = self.sortStr(ele)
            A[ind] = ele

        dc = dict()

        for ind, el in enumerate(A):

            if dc.get(el) is None:
                dc[el] = dc.get(el,[ind+1])

            else:
                dc[el].append(ind+1)

        return list(dc.values())

s = Solution()
print(s.anagrams(["cat","dog","god","tca"]))
