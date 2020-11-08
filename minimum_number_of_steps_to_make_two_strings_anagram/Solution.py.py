'''Given two equal-size strings s and t. In one step you can choose any character of t and replace it with another character.
Return the minimum number of steps to make t an anagram of s.
An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.'''


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dict_n = {}
        for ch in s:
            if ch in dict_n:
                dict_n[ch] += 1
            else:
                dict_n[ch] = 1
        
        count = 0
        for ch in t:
            if ch not in dict_n or dict_n[ch] == 0:
                count += 1
            else:
                dict_n[ch] -= 1
        
        return count