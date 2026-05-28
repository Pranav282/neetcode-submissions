class Solution:
    def climbStairs(self, n):

        if n <= 2:
            return n

        first = 1
        second = 2

        for _ in range(3, n + 1):

            temp = first + second

            first = second
            second = temp

        return second