class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complimentMap = dict()
        for i in range(len(nums)):
            num = nums[i]
            compliment = target - num
            
            if num in complimentMap:
                return [i, complimentMap[num]]
            else:
                complimentMap[compliment] = i