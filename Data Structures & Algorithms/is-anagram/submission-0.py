class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_counter_t = {}
        letter_counter_s = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in letter_counter_s:
                letter_counter_s[s[i]] += 1
            else:
                letter_counter_s[s[i]] = 0
            if t[i] in letter_counter_t:
                letter_counter_t[t[i]] += 1
            else:
                letter_counter_t[t[i]] = 0

        if letter_counter_t == letter_counter_s:
            return True
        else: 
            return False
        