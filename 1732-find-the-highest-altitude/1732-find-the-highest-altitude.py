class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_altitude = 0
        highest = curr_altitude
        
        for altitude_gain in gain:
            curr_altitude += altitude_gain
            highest = max(highest,curr_altitude)
        
        return highest