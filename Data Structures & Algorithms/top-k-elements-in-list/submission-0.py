from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        res = []
        for i in range(k):
            max_key = max(freq, key=freq.get)
            res.append(max_key)
            del freq[max_key]

        return res
        