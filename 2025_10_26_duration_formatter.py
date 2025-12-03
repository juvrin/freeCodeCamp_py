def format(seconds):

    mins = seconds / 60
    hours = 0
    while mins >= 60:
        hours += 1
        mins = mins - 60
        secs = (mins - int(mins)) * 60
    secs = int(round(((mins - int(mins)) * 60), 0))
    mins = int(mins)

    if secs < 10:
        secs_result = "0%d" % secs
    else:
        secs_result = secs

    if mins < 10:
        mins_result = "0%d" % mins
    else:
        mins_result = "%d" % mins

    if hours > 0:
        result = f"{hours}:{mins_result}:{secs_result}"
    else:
        result = f"{mins_result}:{secs_result}"

    return result
