def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    counter = 0
    for times in permanence_period:
        if (type(times[0]) != int or type(times[1]) != int):
            return None
        if times[0] <= target_time <= times[1]:
            counter += 1
    return counter
