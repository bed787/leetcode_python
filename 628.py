class Solution:
    def maximumProduct(self, nums):
        nums.sort()
        product1 = nums[-1] * nums[-2] * nums[-3]
        product2 = nums[0] * nums[1] * nums[-1]
        return max(product1, product2)