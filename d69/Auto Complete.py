import sys


class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.weight = 0
        self.predictions = [("", 0)]*5


class Solution:
    # @param A : list of strings
    # @param B : list of strings
    # @return a list of integers
    def create_Trie(self, A, weight):
        root = TrieNode()
        for ind, ele in enumerate(A):
            curr = root
            for chr in ele:
                if curr.children[ord(chr)-ord('a')] is None:
                    new_node = TrieNode()
                    curr.children[ord(chr)-ord('a')] = new_node
                if curr.predictions[0][1] <= weight[ind]:
                    curr.predictions[0] = (ele, weight[ind])
                    for i in range(4):
                        if curr.predictions[i][1] > curr.predictions[i+1][1]:
                            curr.predictions[i], curr.predictions[i +
                                                                  1] = curr.predictions[i+1], curr.predictions[i]
                        else:
                            break
                curr = curr.children[ord(chr)-ord('a')]
            curr.weight = weight[ind]
            if curr.predictions[0][1] <= weight[ind]:
                curr.predictions[0] = (ele, weight[ind])
                for i in range(4):
                    if curr.predictions[i][1] > curr.predictions[i+1][1]:
                        curr.predictions[i], curr.predictions[i +
                                                              1] = curr.predictions[i+1], curr.predictions[i]
                    else:
                        break
        return root

    def find_in_trie(self, root: TrieNode, A):
        curr = root
        ans = []
        for chr in A:
            if curr.children[ord(chr)-ord('a')] is None:
                return []
            curr = curr.children[ord(chr)-ord('a')]
        ans = curr.predictions
        return ans

    def solve(self, A, B):
        ans = []
        root = self.create_Trie(A)
        for ele in B:
            if self.find_in_trie(root, ele):
                ans.append(1)
            else:
                ans.append(0)
        return ans


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    t = int(input())
    s = Solution()
    while t:
        n, m = input().split()
        n = int(n)
        m = int(m)
        words_list = list(sys.stdin.readline().strip().split())
        weight = list(map(int, sys.stdin.readline().strip().split()))
        prefix = list(sys.stdin.readline().strip().split())
        root = s.create_Trie(words_list, weight)
        for pre in prefix:
            ans = s.find_in_trie(root, pre)
            if len(ans) == 0:
                print(-1, end=" ")
            for ele in ans[::-1]:
                if ele[0] != '':
                    print(ele[0], end=" ")
            print()
        t -= 1
    return 0


if __name__ == '__main__':
    main()
