"""
Clock question. Write a function that takes an input of Hour & Minute. 
Output the angle in degrees of the hands of the clock.
"""

#angle 3-H Hand 12 M-hand 90 = 6 degrees * 15 number of hand positiions between 3 and 12 hand


ANGLE_BETWEEN_SUCCESSIVE_HANDS = 6


def get_total_intervals(hh, mm):
    if mm > hh:
        mm, hh = hh, mm
    
    if hh - mm > 6:
        mm = hh - mm
            
    return abs(hh - mm) * 5 
    

def get_angle(hh, mm):
    # hh - hour hand position
    # mm - minute hand position
    
    return get_total_intervals(hh, mm) * ANGLE_BETWEEN_SUCCESSIVE_HANDS

# 12:00 : h=12, m=0 -> 0
#// 12:15 : h=12, m=15 -> 90
#// 3:00  : h=3, m=0 -> 90
#// 6:00  : h=6, m=0 -> 180
#// 12:30 : h=12, m=30 -> 180

print get_angle(12, 0)
print get_angle(12, 15)
print get_angle(3, 0)
print get_angle(6, 0)                
print get_angle(6, 15)
