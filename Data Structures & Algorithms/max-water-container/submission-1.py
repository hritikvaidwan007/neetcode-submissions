class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        # answer = 47 (because 8 . . . . . . 7) = 787 = 49
        
        # 2 pointers approach:
        max_area = 0 # because max area means max water

        l = 0
        r = len(heights) - 1
        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            if area > max_area:
                max_area = area

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area