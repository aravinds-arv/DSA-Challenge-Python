from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = Counter(nums)
        freq_buckets = [[] for _ in range(len(nums) + 1)]
        
        for num in freq_dict:
            freq = freq_dict[num]
            freq_buckets[freq].append(num)

        res = []
        freq = -1
        while len(res) < k:
            for num in freq_buckets[freq]:
                res.append(num)
            freq -= 1

        return res
