class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        i, j, res = 0, 0, ""

        while i < m and j < n:
            res += word1[i]
            res += word2[j]

            i += 1
            j += 1

        if i < m:
            res += word1[i:]

        if j < n:
            res += word2[j:]

        return res
