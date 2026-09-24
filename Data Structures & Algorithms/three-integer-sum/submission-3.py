class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums  = sorted(nums)
        result = []
        for i in range(len(sorted_nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue

            l = i + 1
            r = len(sorted_nums) - 1
            while l < r : 
                sum = sorted_nums[i] + sorted_nums[l] + sorted_nums[r]
                if sum == 0:
                    result.append([sorted_nums[i],sorted_nums[l],sorted_nums[r]]) 
                    r -= 1
                    l += 1
                    while l < r and sorted_nums[l] == sorted_nums[l-1]:
                        l += 1
                    while l < r and sorted_nums[r] == sorted_nums[r+1]:
                        r -= 1

                elif sum > 0:
                    r -= 1
                else:
                    l += 1

        return result
                                                                  

       
            

            




        