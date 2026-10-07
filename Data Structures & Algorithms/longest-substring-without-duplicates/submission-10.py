class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        right = 0
        hash_set = set()
        count = 0 
        max_count = 0


        while right < len(s): 
            while s[right] in hash_set:
                hash_set.remove(s[left])
                count -= 1
                left += 1 

            hash_set.add(s[right])
            count += 1
            max_count = max(count, max_count)
            right += 1 

        return max_count
