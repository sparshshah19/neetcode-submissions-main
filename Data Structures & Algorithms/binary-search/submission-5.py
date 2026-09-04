class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #so how binary search works is you want to compute the middle, 
        left = 0 
        right = len(nums) - 1
        
        while left <= right: 
            middle = (left + right) // 2
            if nums[middle] < target: 
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        
        return -1 

