class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_set = set(nums)
        for num in nums_set:
            if nums.count(num) > len(nums) / 2:
                return num
            pass
