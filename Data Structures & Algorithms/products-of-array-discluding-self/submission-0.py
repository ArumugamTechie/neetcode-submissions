class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = []
        pre_prod = 1
        double_zero = False
        res = [0] * len(nums)
        for i,num in enumerate(nums):
            if num == 0:
                zeros.append(i)
            else:
                pre_prod *= num

            if len(zeros) > 1:
                return [0] * len(nums)

        if len(zeros) == 1:
            res[zeros[0]] = pre_prod
            return res 

        for i,num in enumerate(nums):
            mul = pre_prod // num
            res[i] = mul

        return res
            

        