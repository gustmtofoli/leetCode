''' Given a string s, find the length of the longest substring without repeating characters. '''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        sett = set()
        ans = 0
        i = 0
        j = 0
        while i < n and j < n:
            if s[j] not in sett:
                sett.add(s[j])
                j += 1
                ans = max(ans, j - i)
            else:
                sett.remove(s[i])
                i += 1
        return ans

'''
Approach: sliding window

Time complexity: O(n)
'''