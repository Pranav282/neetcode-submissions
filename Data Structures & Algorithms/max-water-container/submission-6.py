class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        max_vol = 0
        
        for i in range(n):
            j = n - 1

            while i < j:
                height = min ( heights[i], heights[j] )
                width = ( j - i )
                current_vol = height * width

                max_vol = max(current_vol, max_vol)
                j-=1

        return max_vol