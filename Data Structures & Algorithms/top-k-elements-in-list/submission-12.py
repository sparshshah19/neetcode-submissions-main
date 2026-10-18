class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #top_k_frequent_elenents 


        freq_map = {}

        for num in nums: 
            freq_map[num] = 1 + freq_map.get(num, 0)


        #1:1 
        #2:2
        #3:3

        ls = list()
        for key, val in freq_map.items(): 
            ls.append([val, key])
        ls.sort(reverse = True)
        
        result = []
        for i in range(k): 
            result.append(ls[0][1])
            ls.pop(0)
        return result 
            


        #[3,3], [2,2], [1,1]
