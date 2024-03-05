#Question 1
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        elems = set()
        for elem in nums:
            if elem in elems:
                return True
            else:
                elems.add(elem)
        return False

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        num_clips = 0
        clips_start = 1000
        clips_end = 0
        clips.sort()
        for clip in clips:
            if clip[0] <= clips_start and clip[1] >= clips_end:
                clips_start = clip[0]
                clips_end = clip[1]
            elif clip[1] >= clips_end:
                clips_end = clip[1]
                num_clips +=1
        if clips_start != 0 and clips_end != time:
            num_clips = -1
        return num_clips

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        ans=0
        while left<right:
            min_=min(height[left],height[right])*(right-left)
            ans=max(ans,min_)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return ans

