from collections import Counter

class Solution:
    def letterToNum(self, letter: str) -> int:
        return ord(letter.upper()) - ord('A')

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_map = dict()
        for string in strs:
            freq_list = [0] * 26
            for letter in string:
                n = self.letterToNum(letter)
                freq_list[n] += 1
            
            freq_tup = tuple(freq_list)
            freq_map[freq_tup] = freq_map.get(freq_tup, []) + [string]
        
        return list(freq_map.values())
