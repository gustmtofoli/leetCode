''' Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.'''


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        if n <= 1:
            return 0
        
        maxLeft = [None]*n
        maxRight = [None]*n
        
        maxLeft[0] = height[0]
        for i in range(1, n):
            maxLeft[i] = max(height[i], maxLeft[i-1])
        
        maxRight[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            maxRight[i] = max(height[i], maxRight[i+1])
        
        count = 0
        print(maxLeft)
        print(maxRight)
        for i in range(n):
            count += min( maxLeft[i], maxRight[i]) - height[i]
        
        return count

'''
Approach: Dynamic programming:
    1. Find the max heights from left to right end;
    2. Find the max heights from right to left end;
    3. Find the minimum between the two max heights (left to end and right to end) and substract the current height from the the value

Time complexity: O(n)
'''