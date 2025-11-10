def breakdown_time(seconds):
    if type(seconds) != int or seconds <0:
        return -1
    if seconds == 0:
        return {}
    units=[3600,60,1]
    result = {}
    remaining = seconds
    for unit in units:
        count = remaining // unit
        if count >0:
            result[unit] = count
        remaining = remaining % unit
    return result
print(breakdown_time(7200))
