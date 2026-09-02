class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter = {} 
        for s in strs:
            letters = [0] * 26
            for k in s:
                letters[ord(k) - ord("a")] += 1
            if tuple(letters) in counter:
                counter[tuple(letters)].append(s)
            else:
                counter[tuple(letters)] = [s]
        return list(counter.values())


                
                
        