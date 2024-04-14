# return the total byte size of the object.
def total_bytes(obj):
    return obj.__sizeof__()
print(total_bytes('[":)", 1]'))
