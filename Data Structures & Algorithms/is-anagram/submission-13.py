class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #anagrams 
        #hashmaps use anagrams 

        #count the frequency of each, and if the frequencies of each character is the same, 
        #it's true

        if len(s) != len(t): 
            return False

        
        count_t = {}
        count_s = {}   

        for i in range(len(s)): 
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
            count_s[s[i]] = 1 + count_s.get(s[i], 0)

        return count_t == count_s

        #count_t hashmap 

        #c : 2
        #a : 2
        #r : 2 
        #e : 1

