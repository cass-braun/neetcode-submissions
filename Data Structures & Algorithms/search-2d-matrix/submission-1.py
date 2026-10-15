class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        def bs(start, end, mid):
            startR = start // cols
            startC = start% cols

            endR = end //cols
            endC = end % cols

            midR = mid // cols
            midC = mid % cols

            if matrix[midR][midC] == target:
                return True

            if -1 <= start - end <= 1:
                if matrix[startR][startC] == target:
                    return True
                if matrix[endR][endC] == target:
                    return True
                return False
            
            if target > matrix[midR][midC]:
                newMid = (mid + end) //2
                return bs(mid,end, newMid)
            elif target < matrix[midR][midC]:
                newMid = (mid + start) //2
                return bs(start, mid, newMid)
        
        return bs(0, rows*cols-1, (rows*cols-1)//2)
