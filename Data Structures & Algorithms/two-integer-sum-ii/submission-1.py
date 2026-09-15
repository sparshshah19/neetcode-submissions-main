class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #we have to use two pointers in this.
        #what two pointers tell us is we have to see if its greater 

        left = 0 
        right = len(numbers) - 1 

        while left < right: 
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else: 
                return [left + 1, right + 1]