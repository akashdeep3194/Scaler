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

    def match_len(self, ele, root):
        curr = root
        l = 0
        for chr in ele:
            if curr.children[ord(chr)-ord('a')] is None:
                return l
            curr = curr.children[ord(chr)-ord('a')]
            l += 1
        return l

    def find_modified_in_trie(self, ele, root):
        common = self.match_len(ele, root)
        if len(ele) == common:
            common -= 1
        for i in range(common+1):
            for letter in range(ord('a'), ord('z')+1):
                if chr(letter) == ele[i]:
                    continue
                letter = chr(letter)
                mod_ele = ele[0:i] + letter + ele[i+1:]
                if self.find_in_trie(root, mod_ele):
                    return "1"
        return "0"

    def rec_find_modified(self, root: TrieNode, ele, ind, mismatch):
        if mismatch < 0:
            return False
        if len(ele) == ind+1:
            char_zero = ord(ele[ind]) - ord('a')
            if mismatch == 0:
                if root.children[char_zero] == None:
                    return False
                elif root.children[char_zero].isEnd == True:
                    return True
                else:
                    return False
            else:
                for i in range(26):
                    if i != char_zero and root.children[i] != None and root.children[i].isEnd == True:
                        return True
                return False
        char_zero = ord(ele[ind]) - ord('a')
        for i in range(26):
            if root.children[i] == None:
                continue
            if i == char_zero:
                small_ans = self.rec_find_modified(
                    root.children[i], ele, ind+1, mismatch)
            else:
                small_ans = self.rec_find_modified(
                    root.children[i], ele, ind+1, mismatch-1)
            if small_ans:
                return True
        return False

    def solve(self, A, B):
        ans = ""
        root = self.create_Trie(A)
        for ele in B:
            if self.rec_find_modified(root, ele, 0, mismatch=1):
                ans += "1"
            else:
                ans += "0"
        return ans


if __name__ == "__main__":
    s = Solution()
    A = ["data", "circle", "cricket"]
    B = ["date", "circel", "crikket", "data", "circl"]
    print(s.solve(A, B))
