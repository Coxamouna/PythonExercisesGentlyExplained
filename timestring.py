def getTimeString(totalSeconds):
    # if totalSeconds is 0, just return '0s':
    if (totalSeconds == 0):
        return '0s'
    # set hours to 0. then add an hour for every 3600 seconds removed from
    # totalSeconds until totalSeconds is less than 3600:
    hours = 0
    while totalSeconds >= 3600:
        hours += 1
        totalSeconds -= 3600
    # set days to 0. then add a day for every 24 hours removed from
    # hours until hours is less than 24:
    days = 0
    while hours >= 24:
        days += 1
        hours -= 24
    # set minutes ot 0. then add a minute for every 60 seconds removed
    # from totalSeconds until totalSeconds is less than 60:
    minutes = 0
    while totalSeconds >= 60:
        minutes += 1
        totalSeconds -= 60
    # set seconds to the remaining totalSeconds value:
    seconds = totalSeconds
    
    # create an empty list hms that will store the string days/hour/minute/second:
    hms = []
    # if there are one or more days, add the amount with a 'd' suffix:
    if days >= 1:
        hms.append(str(days) + 'd')
    # if there are one or more hours, add the amount with an 'h' suffix:
    if hours >= 1:
        hms.append(str(hours) + 'h')
    # if there are one or more minutes, add the amount with an 'm' suffix:
    if minutes >= 1:
        hms.append(str(minutes) + 'm')
    # if there are one or more seconds, add the amount with an 's' suffix:
    if seconds >= 1:
        hms.append(str(seconds) + 's')
    
    # join the hour/minute/second strings together with a space in between them:
    return ' '.join(hms) 

print(getTimeString(42069))
        
assert getTimeString(30) == '30s'
assert getTimeString(60) == '1m'
assert getTimeString(90) == '1m 30s'
assert getTimeString(3600) == '1h'
assert getTimeString(3601) == '1h 1s'
assert getTimeString(3661) == '1h 1m 1s'
assert getTimeString(90042) == '1d 1h 42s'
assert getTimeString(0) == '0s'
