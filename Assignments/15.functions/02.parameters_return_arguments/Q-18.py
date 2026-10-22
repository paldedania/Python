# 18. Define convert_minutes(minutes, seconds_per_minute=60) that returns the total seconds.

def convert_minutes(minutes, seconds_per_minute=60):
    return minutes * seconds_per_minute


print(convert_minutes(5))
print(convert_minutes(2, seconds_per_minute=60))
