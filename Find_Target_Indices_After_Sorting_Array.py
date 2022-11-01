class Solution(object):
    def targetIndices(self, nums, target):
       
        res=[]
        
        nums.sort()
        print(nums)
        for num in range(len(nums)):
            if nums[num] == target:
                res.append(num)
        return res