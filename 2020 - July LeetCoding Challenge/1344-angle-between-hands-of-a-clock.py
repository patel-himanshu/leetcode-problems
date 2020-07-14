# Question: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/545/week-2-july-8th-july-14th/3390/

"""
Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.

Example 1:
    Input: hour = 12, minutes = 30
    Output: 165

Example 2:
    Input: hour = 3, minutes = 30
    Output: 75

Example 3:
    Input: hour = 3, minutes = 15
    Output: 7.5

Example 4:
    Input: hour = 4, minutes = 50
    Output: 155

Example 5:
    Input: hour = 12, minutes = 0
    Output: 0

Constraints:
    (1) 1 <= hour <= 12
    (2) 0 <= minutes <= 59
    (3) Answers within 10^-5 of the actual value will be accepted as correct.
"""

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        HOUR = 0.5 # Angle made by hour hand per minute
        MINUTE = 6 # Angle made by minute hand per minute
        
        if hour == 12:
            hour = 0
        
        hour_angle = hour * 30 + minutes * HOUR
        minute_angle = minutes * MINUTE
        
        diff = abs(minute_angle - hour_angle)
        return min(diff, 360 - diff)