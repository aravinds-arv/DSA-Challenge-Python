class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = strs[0]
        for i in range(1, len(strs)):
            while lcp not in strs[i] and len(lcp) > 0:
                lcp = lcp[:-1]

        return lcp