class Solution:
    def maxArea(self, heights: List[int]) -> int:

        i = 0
        j = len(heights) - 1

        max_area = 0

        while i < j:

            height = min(heights[i], heights[j])
            width = j - i

            current_area = height * width

            max_area = max(max_area, current_area)

            # move smaller height
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return max_area