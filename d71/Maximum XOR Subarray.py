class TrieNode():
    def __init__(self):
        self.index = -1
        self.child = [None]*2


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def insert_in_Trie(self, root, ele, index):
        for char in ele:
            if root.child[int(char)] == None:
                root.child[int(char)] = TrieNode()
            root = root.child[int(char)]
        root.index = index

    def find_xor_in_Trie(self, root, ele):
        ans = 0
        i = 31
        for char in ele:
            if root.child[1-int(char)] == None:
                root = root.child[int(char)]
            else:
                root = root.child[1-int(char)]
                ans += (2**i)
            i -= 1
        return ans, root.index+1

    def solve(self, A):
        pf_xor = []
        x = 0
        answer = ans = 0
        for ind, ele in enumerate(A):
            x = ele ^ x
            pf_xor.append(x)
            if answer < x:
                answer = x
                index = [1, ind+1]
        root = TrieNode()

        for ind, ele in enumerate(pf_xor):
            num = ""
            while ele > 0:
                num = str(ele & 1) + num
                ele = ele >> 1
            num = "0"*(32-len(num)) + num

            if ind == 0:
                self.insert_in_Trie(root, num, 0)
                continue

            ans, si = self.find_xor_in_Trie(root, num)
            self.insert_in_Trie(root, num, ind)
            if answer == ans:
                if index[1]-index[0] > ind-si:
                    index = [si+1, ind+1]
                elif index[1]-index[0] == si-ind:
                    if si+1 < index[0]:
                        index = [si+1, ind+1]
            if answer < ans:
                answer = ans
                index = [si+1, ind+1]
        return index
