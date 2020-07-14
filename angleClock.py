class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:

        hour_angle = ( hour * 30 ) + minutes/2
        minute_angle = minutes * 6
        
        angle_diff = abs(hour_angle - minute_angle)

        return angle_diff if angle_diff <= 180 else 360 - angle_diff
