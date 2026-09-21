class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window 
        count = 0
        max_count = 0
        left = 0
        right = 0
        hash_set = set()
    
        #set = x, y, z
        #count = 3
        #left = 2
        #right = 4, s[right] = x
        #max_count = 3
        #if the characters in the window are different 
        #we will make the window one more 
        
        while right < len(s):
            while s[right] in hash_set:
                hash_set.remove(s[left])
                left += 1
            hash_set.add(s[right])
            max_count = max(right - left + 1, max_count)
            right += 1 
            
       
        return max_count 