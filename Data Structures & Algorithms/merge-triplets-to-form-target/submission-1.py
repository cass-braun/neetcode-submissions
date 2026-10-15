class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        targetDict = {
            0: False,
            1: False,
            2: False,
        }

        for index, triplet in enumerate(triplets):
            
            fulfillsIndices = []

            tooHigh = False
            j = 0

            while not tooHigh and j < 3:
                if triplet[j] > target[j]:
                    tooHigh = True
                if triplet[j] == target[j]:
                    fulfillsIndices.append(j)

                j+=1
            print(triplet)
            print(fulfillsIndices)
            print('***')
            if not tooHigh:
                for f in fulfillsIndices:
                    if not targetDict[f]:
                        targetDict[f] = True
            if targetDict[0] and targetDict[1] and targetDict[2]:
                return True


        return targetDict[0] and targetDict[1] and targetDict[2]
                
