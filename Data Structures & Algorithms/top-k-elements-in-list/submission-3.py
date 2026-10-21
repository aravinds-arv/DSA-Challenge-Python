from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = Counter(nums)
        freq_buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in freq_dict.items():
            freq_buckets[freq].append(num)

        res = []
        for freq in range(len(freq_buckets) - 1, 0, -1):
            for num in freq_buckets[freq]:
                res.append(num)
                k -= 1
                if k == 0:
                    return res
