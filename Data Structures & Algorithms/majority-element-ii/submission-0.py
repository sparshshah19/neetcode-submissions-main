class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #nums integer of size n 
        #find all elements that appear more than n/3 times absolute value

        threshold = len(nums) / 3
        hash_map = {}  
        ans = []

        #count frequency 

        #and wherever the frequency is greater then the threshold we will 
           #add that key to the hashmap 

        for num in nums: 
            hash_map[num] = 1 + hash_map.get(num, 0)
        
        for key, val in hash_map.items():
            if val > threshold: 
                ans.append(key)
            
        return ans 
        #5: 4
        #2: 5
        #3: 1


