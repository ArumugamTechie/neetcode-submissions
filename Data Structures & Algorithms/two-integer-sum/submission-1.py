class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pre_sum = {}
        # two pass  -- approach

        # for i in range(len(nums)):
        #     pre_sum[nums[i]] = i
        
        # for i in range(len(nums)):
        #     diff = target - nums[i]
        #     if diff in pre_sum and pre_sum[diff] != i:
        #         return [i,pre_sum[diff]]

        # one pass approach

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in pre_sum:
                return [pre_sum[diff],i]
            pre_sum[nums[i]] = i




        