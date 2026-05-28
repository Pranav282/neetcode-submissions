class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        #handling edge cases
        if n == 0:
            return 0

        if n == 1:
            return nums[0]

        output = [0] * n

        output[0] = nums[0]

        #second house 
        output[1] = max(nums[0], nums[1])

        for i in range(2, n):

            output[i] = max(
                output[i-1],
                nums[i] + output[i-2]
            )

        return output[n-1]