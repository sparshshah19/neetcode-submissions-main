class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_map = {} 
        for i, n in enumerate(nums):
            needed = target - n
            if needed in num_map: 
                return [num_map[needed], i]
            else:
                num_map[n] = i
            