class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #division operation 

        #result = [0] * len(nums)

        #for i in range(len(nums)):
          #  product = 1 
          #  for j in range(len(nums)): 
          #      if i == j: 
          #          continue
           #     product *= nums[j]
            
         #   result[i] = product 
     #   return result


        #prefix suffix 

        arr = [0] * len(nums)
        prefix = 1
        for i in range(len(nums)): 
            arr[i] = prefix
            prefix *= nums[i]
        
        suffix = 1 
        for i in range(len(nums) -1, -1, -1): 
            arr[i] *= suffix 
            suffix *= nums[i]
            
        
        return (arr)