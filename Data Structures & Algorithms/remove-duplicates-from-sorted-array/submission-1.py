class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0

        while r < len(nums):
            if nums[r] != nums[l]:
                l += 1
                if r != l:
                    nums[l] = nums[r]
            r += 1

        return l + 1
