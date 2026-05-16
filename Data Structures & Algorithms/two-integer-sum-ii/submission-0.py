class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        unique=set(numbers)
        output=[]
        for i in range(len(numbers)):
            residual = target - numbers[i]
            if residual in unique:
                output.append(i+1)
                output.append(numbers.index(residual)+1)
                return output