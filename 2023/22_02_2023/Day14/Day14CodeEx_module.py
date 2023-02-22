start_range = 0
end_range = 100
def water_state(temp):
    if temp <= start_range:
        return "Solid"
    elif start_range < temp < end_range:
        return "Liquid"
    else:
        return "Gas"
