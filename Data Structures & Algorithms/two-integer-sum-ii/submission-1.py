class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers)-1

        currentSum = numbers[start] +numbers[end]

        while currentSum != target:
            
            if (currentSum < target):
                start += 1
            elif(currentSum > target):
                end -= 1
            currentSum = numbers[start] +numbers[end]
        

        return [start+1, end+1]
