class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # zeros = []
        # pre_prod = 1
        # res = [0] * len(nums)
        # for i,num in enumerate(nums):
        #     if num == 0:
        #         zeros.append(i)
        #     else:
        #         pre_prod *= num

        #     if len(zeros) > 1:
        #         return [0] * len(nums)

        # if len(zeros) == 1:
        #     res[zeros[0]] = pre_prod
        #     return res 

        # for i,num in enumerate(nums):
        #     mul = pre_prod // num
        #     res[i] = mul

        # return res
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1

        for i in range(len(nums) - 1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
        
            

        