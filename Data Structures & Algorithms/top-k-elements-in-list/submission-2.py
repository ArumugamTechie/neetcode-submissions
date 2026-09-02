class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        out = []
        freq_counter = {}
        freq = []
        for i in range(len(nums)+1):
            freq.append([])

        for i in nums:
            if i in freq_counter:
                freq_counter[i]+=1
            else:
                freq_counter[i] = 1

        for key,v in freq_counter.items():

            freq[v].append(key)

        for l in range(len(freq) -  1 , 0 , -1):
            for i in freq[l]:
                out.append(i)
                if len(out) == k:
                    return out
        return out





        

