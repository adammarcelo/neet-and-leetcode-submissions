class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            max_height = min(heights[l], heights[r])
            max_width = r - l
            max_area = max(max_area, max_height * max_width)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return max_area