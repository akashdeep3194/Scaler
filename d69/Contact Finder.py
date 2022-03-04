class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.freq = 0


class Solution:
    # @param A : list of strings
    # @param B : list of strings
    # @return a list of integers
    def insert_in_Trie(self, root, ele):
        curr = root
        for chr in ele:
            if curr.children[ord(chr)-ord('a')] is None:
                new_node = TrieNode()
                curr.children[ord(chr)-ord('a')] = new_node
            curr.freq += 1
            curr = curr.children[ord(chr)-ord('a')]
        curr.freq += 1
        return root

    def find_in_trie(self, root, A):
        curr = root
        for chr in A:
            if curr.children[ord(chr)-ord('a')] is None:
                return 0
            curr = curr.children[ord(chr)-ord('a')]
        return curr.freq

    def solve(self, A, B):
        ans = []
        root = TrieNode()
        for i, ele in enumerate(B):
            if A[i] == 0:
                self.insert_in_Trie(root, ele)
            else:
                ctr = self.find_in_trie(root, ele)
                ans.append(ctr)
        return ans


if __name__ == "__main__":
    s = Solution()
    A = [0, 1]
    B = ["abcde", "abc"]
    print(s.solve(A, B))
