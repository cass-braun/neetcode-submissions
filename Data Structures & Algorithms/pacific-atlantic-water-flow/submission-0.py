class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pacific_borders = set()
        atlantic_borders = set()

        for r in range(rows):
            pacific_borders.add((r, 0))

            atlantic_borders.add((r, cols-1))

        for c in range(cols):
            pacific_borders.add((0, c))

            atlantic_borders.add((rows-1, c))

        pacific = set()
        atlantic = set()

        def findStuff(i, j, ocean):
            if i+1 < rows and heights[i+1][j] >= heights[i][j] and (i+1, j) not in ocean:
                ocean.add((i+1, j))
                findStuff(i+1, j, ocean)

            if i-1 > -1 and heights[i-1][j] >= heights[i][j] and (i-1, j) not in ocean:
                ocean.add((i-1, j))
                findStuff(i-1, j, ocean)

            if j+1 < cols and heights[i][j+1] >= heights[i][j] and (i, j+1) not in ocean:
                ocean.add((i, j+1))
                findStuff(i, j+1, ocean)

            if j-1 > -1 and heights[i][j-1] >= heights[i][j] and (i, j-1) not in ocean:
                ocean.add((i, j-1))
                findStuff(i, j-1, ocean)
                

        for i, j in pacific_borders:
            pacific.add((i,j))
            findStuff(i, j, pacific)
        
        for i, j in atlantic_borders:
            atlantic.add((i,j))
            findStuff(i, j, atlantic)
        
        return [ [r, c] for r,c in pacific & atlantic]




        