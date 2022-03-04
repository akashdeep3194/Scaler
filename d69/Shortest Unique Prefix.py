from sys import prefix


class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.freq = 0


class Solution:
    # @param A : list of strings
    # @param B : list of strings
    # @return a list of integers
    def create_Trie(self, A):
        root = TrieNode()
        for ele in A:
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
        ans = ""
        for chr in A:
            if curr.children[ord(chr)-ord('a')] is None:
                return ""
            curr = curr.children[ord(chr)-ord('a')]
            ans += chr
            if curr.freq == 1:
                return ans
        return ans

    def prefix(self, A):
        ans = []
        root = self.create_Trie(A)
        for ele in A:
            prefix = self.find_in_trie(root, ele)
            ans.append(prefix)
        return ans


if __name__ == "__main__":
    s = Solution()
    A = ["bat", "ball", "car"]
    print(s.prefix(A))
