class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights) - 1
        max_area = 0

        #width = right - left 
        #height = min(heights[right], heights[left])
        #area = (min(heights[right], heights[left])) * (right - left)
        #max_area = max(area, max_area)

        while left < right: 
            area = (min(heights[right], heights[left])) * (right - left)
            if heights[right] >= heights[left]:
                left += 1
            else: 
                right -= 1
            max_area = max(area, max_area)
        return max_area
        
            #at the furthest point, start. 
            #width is maximized. 
            #if the height is greater than before, we could get a better max. 
            #if the height is smaller than we are at the best solution. 

            #if we move left to the right, so left += 1, our area decreases only if height doesn't increase. 

            #so if heights[right] >= heights[left] 
                #left += 1 
                #if heights[left] > heights[right]
                #right -= 1