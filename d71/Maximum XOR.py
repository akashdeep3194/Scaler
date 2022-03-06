class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.child = [None]*2


class Solution:
    # @param A : list of integers
    # @return an integer
    def insert_in_Trie(self, root: TrieNode, ele):
        for char in ele:
            if root.child[int(char)] == None:
                root.child[int(char)] = TrieNode()
            root = root.child[int(char)]
        root.isEnd = True

    def find_xor_in_Trie(self, root: TrieNode, ele):
        ans = 0
        i = 31
        for char in ele:
            if root.child[1-int(char)] != None:
                ans += (2**i)*1
                root = root.child[1-int(char)]
            elif root.child[int(char)] != None:
                root = root.child[int(char)]
            else:
                return ans
            i -= 1
        return ans

    def solve(self, A):
        answer = ans = 0
        root = TrieNode()
        for ele in A:
            num = ""
            while (ele > 0):
                num = str(ele & 1) + num
                ele = ele >> 1
            num = "0"*(32-len(num)) + num
            ans = self.find_xor_in_Trie(root, num)
            self.insert_in_Trie(root, num)
            answer = max(ans, answer)
        return answer
