class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = {}
        for i, n in enumerate(sorted(nums)):
            if n not in result:
                result[n] = i
                
        return [result[n] for n in nums]