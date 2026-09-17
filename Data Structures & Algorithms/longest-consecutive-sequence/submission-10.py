class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        longest = 0 
        length = 0
        for num in seen: 
            if num - 1 not in seen: 
                length = 1
                while num + 1 in seen: 
                    length += 1 
                    num = num + 1
            longest = max(length, longest)
        return longest

        