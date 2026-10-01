class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dick = {}
        for i, num in enumerate(nums):
            if num in dick:
                return [dick[num], i]
            
            diff = target - num
            dick[diff] = i
            
        
