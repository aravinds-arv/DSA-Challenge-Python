class Solution:
    def letterToNum(self, letter: str) -> int:
        return ord(letter) - ord('a')

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_map = defaultdict(list)
        for string in strs:
            freq_list = [0] * 26
            for letter in string:
                n = self.letterToNum(letter)
                freq_list[n] += 1
            
            freq_map[tuple(freq_list)].append(string)
        
        return list(freq_map.values())
