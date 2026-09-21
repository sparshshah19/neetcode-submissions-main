class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #put it into a hashmap 
        #and then just find the char with the largest # and add k and return 
        #that output
        best = 0 
        max_best = 0
        left = 0 
        right = 0
        hash_map = defaultdict(int)
        while right < len(s):
            hash_map[s[right]] += 1 

            while (right - left + 1) - max(hash_map.values()) > k: 
                hash_map[s[left]] -= 1
                left += 1

            best = right - left + 1
            max_best = max(best, max_best)
            right += 1

        return max_best
        #X: 2 
        #Y: 2