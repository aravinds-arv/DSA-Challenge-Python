class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        preProd = 1
        for i in range(n):
            res[i] = preProd
            preProd *= nums[i]
        
        postProd = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postProd
            postProd *= nums[i]

        return res
