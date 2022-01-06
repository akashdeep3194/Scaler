from typing import List
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:

        if len(sentences) == 0:
            return 0

        countmx = 0

        for sentence in sentences:
            if len(sentence) == 0:
                count = 0
                continue
            count = 1
            for ele in sentence:
                if ele == " ":
                    count += 1
            countmx = max(count,countmx)

        return countmx

s = Solution()
print(s.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))
