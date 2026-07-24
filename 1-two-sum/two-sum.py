class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i in range(0,len(nums)):
            t = target - nums[i]
            if t in table.keys():
                return [i,table[t]]
            else:
                table[nums[i]] = i

                
        