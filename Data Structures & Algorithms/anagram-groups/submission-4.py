class Solution:
    def letterToNum(self, letter: str) -> int:
        return ord(letter.upper()) - ord('A')

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_map = dict()
        for string in strs:
            freq_tup = (0, ) * 26
            for letter in string:
                n = self.letterToNum(letter)
                freq_tup = freq_tup[0:n] + ((freq_tup[n] + 1), ) + freq_tup[n+1:]
            
            freq_map[freq_tup] = freq_map.get(freq_tup, []) + [string]
        
        return list(freq_map.values())
