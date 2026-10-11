class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        strs.sort()

        lcp = strs[0]
        while len(lcp) > 0:
            if strs[-1].startswith(lcp):
                return lcp
            lcp = lcp[:-1]
        
        return lcp
