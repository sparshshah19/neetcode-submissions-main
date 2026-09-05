class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [] 
        #prefix and suffix 
        #prefix * suffix is gonna be the result
        prefix = 1
        #prefix pass

        for i in range(len(nums)):
            ans.append(prefix)
            prefix *= nums[i]
        

        #[1,1,2,8]
        postfix = 1 
        #postfix pass
        for i in range(len(nums) - 1, -1, -1): 
            ans[i] *= postfix
            postfix *= nums[i]
        
        return ans

        