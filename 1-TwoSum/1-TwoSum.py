# Last updated: 1/29/2026, 5:55:04 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            current_number = nums[i]
            needed_number = target - current_number
            if needed_number in seen:
                return [seen[needed_number],i]
            seen[current_number]=i
        