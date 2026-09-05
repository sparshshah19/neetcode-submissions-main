class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        columns = len(matrix[0])

        for r in range(rows):
            for c in range(columns):
                if matrix[r][c] == target:
                    return True
        return False
            
        ''' o_lvl_left = 0 
        #o_lvl_right = len(matrix) - 1

        while o_lvl_left <= o_lvl_right:
            mid_o_matrix = (o_lvl_left + o_lvl_right) // 2
            
            i_lvl_left = 0 
            i_lvl_right = len(matrix[mid_o_matrix]) - 1

            while i_lvl_left <= i_lvl_right:
                middle = (i_lvl_left + i_lvl_right) // 2
                if matrix[mid_o_matrix][middle] > target:
                    i_lvl_right = middle - 1
                elif matrix[mid_o_matrix][middle] < target:
                    i_lvl_left = middle + 1
                else: 
                    return True
        
        return False

    #middle list
    #middle of the middle and run binary serarch 

    #[1,2,4,5] target = 4
        '''