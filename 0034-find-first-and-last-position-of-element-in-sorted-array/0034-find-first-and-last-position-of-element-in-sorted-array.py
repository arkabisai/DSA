class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []
        
        if target not in nums:
            return [-1, -1]
        else:
            for i in range(len(nums)):
                if nums[i] == target:
                    result.append(i)
                    break
            for j in reversed(range(len(nums))):
                if nums[j] == target:
                    result.append(j)
                    break
        return result