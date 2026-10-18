class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #given a list 
        ans_ls = []

        #return a list of lists 
        result = defaultdict(list) #charactercount to list of anagrams 

        for word in strs: 
            freq_map = {}
            for char in word: 
                freq_map[char] = 1 + freq_map.get(char, 0)
            result[tuple(sorted(freq_map.items()))].append(word)
        
        for val in result.values():
            ans_ls.append(val)
        
        return ans_ls
