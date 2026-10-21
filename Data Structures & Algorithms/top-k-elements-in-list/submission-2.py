from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = Counter(nums)
        freq_buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in freq_dict.items():
            freq_buckets[freq].append(num)

        res = []
        freq = -1
        while k > 0:
            for num in freq_buckets[freq]:
                res.append(num)
                k -= 1
            freq -= 1

        return res
