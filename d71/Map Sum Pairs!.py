class TrieNode():
    def __init__(self):
        self.child = [None]*26
        self.freq = 0
        self.isEnd = False


class Solution:
    # @param A : list of strings
    # @param B : list of integers
    # @return a list of integers
    def insert_in_Trie(self, root, ele, val, rev=False):
        rooter = root
        for char in ele:
            if root.child[ord(char) - ord('a')] == None:
                root.child[ord(char)-ord('a')] = TrieNode()
            root = root.child[ord(char)-ord('a')]
            if rev == False:
                root.freq += val
            else:
                root.freq -= val

        if rev == True:
            return

        if root.isEnd == True:
            j = 0
            sm = 0
            while j < 26:
                if root.child[j] != None:
                    sm += root.child[j].freq
                j += 1
            old_val = root.freq - sm - val
            self.insert_in_Trie(rooter, ele, old_val, rev=True)
        root.isEnd = True

    def find_prefix_in_Trie(self, root, ele):
        for char in ele:
            if root.child[ord(char) - ord('a')] == None:
                return 0
            root = root.child[ord(char)-ord('a')]

        return root.freq

    def solve(self, A, B):
        root = TrieNode()
        ans = []
        for i in range(len(A)):
            if B[i] == -1:
                ans.append(self.find_prefix_in_Trie(root, A[i]))
            else:
                val = B[i]
                self.insert_in_Trie(root, A[i], val)
        return ans
