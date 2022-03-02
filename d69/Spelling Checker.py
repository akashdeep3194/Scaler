class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False


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
                curr = curr.children[ord(chr)-ord('a')]
            curr.isEnd = True
        return root

    def find_in_trie(self, root, A):
        curr = root
        for chr in A:
            if curr.children[ord(chr)-ord('a')] is None:
                return False
            curr = curr.children[ord(chr)-ord('a')]
        return curr.isEnd == True

    def solve(self, A, B):
        ans = []
        root = self.create_Trie(A)
        for ele in B:
            if self.find_in_trie(root, ele):
                ans.append(1)
            else:
                ans.append(0)
        return ans


if __name__ == "__main__":
    s = Solution()
    A = ["bat", "ball", "car"]
    B = ["bat", "bag"]
    s.solve(A, B)
