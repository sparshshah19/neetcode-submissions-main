class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0 
        #it is sorted
        right = len(numbers) - 1

        while left < right: 
            evaluation = numbers[left] + numbers[right]
            if evaluation > target: 
                right -= 1
            elif evaluation < target:
                left += 1
            else: 
                return [left + 1, right + 1]
        
        