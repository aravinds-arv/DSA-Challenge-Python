class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        
        while nums and k < len(nums):
            if nums[k] == val:
                del nums[k]
            else:
                k += 1

        return k
        