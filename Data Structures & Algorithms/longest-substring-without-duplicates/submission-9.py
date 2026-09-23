class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0 
        right = 0
        max_count = 0
        hash_set = set()

        #hash_set [z]
        while right < len(s): 
            #while invalid 
            while s[right] in hash_set: 
                hash_set.remove(s[left])
                left += 1
                
            
            hash_set.add(s[right])
            max_count = max(right - left + 1, max_count)
            right += 1

        return max_count