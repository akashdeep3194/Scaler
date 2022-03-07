class TrieNode():
    def __init__(self):
        self.child = [None]*26
        self.isEnd = False


class Solution:
    # @param A : list of strings
    # @return an integer
    def insert_in_Trie(self, root, ele):
        created = 0
        for char in ele:
            ind = ord(char)-ord('0')
            if root.isEnd == True:
                return False
            if root.child[ind] == None:
                root.child[ind] = TrieNode()
                created = 1
            root = root.child[ind]
        if created == 0:
            return False
        root.isEnd = True
        return True

    def solve(self, A):
        root = TrieNode()
        for ele in A:
            ans = self.insert_in_Trie(root, ele)
            if not ans:
                return 0
        else:
            return 1
