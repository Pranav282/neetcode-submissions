class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        output = [0] * n

        output[0] = cost[0]
        output[1] = cost[1]

        for i in range(2, n):
            output[i] = cost[i] + min(
                output[i-1],
                output[i-2]
            )

        return min(output[n-1], output[n-2])