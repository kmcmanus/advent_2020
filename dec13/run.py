import math
import functools

with open('input', 'r') as f:
    time = int(f.readline().strip())
    busses = [
        int(line.strip())
        for line in f.readline().split(",")
        if 'x' not in line
    ]

avail = {
    bus: (math.floor(time/bus) + 1) * bus
    for bus in busses
}

def selection(nxt, curr):
    (nxt_bus, nxt_time) = nxt
    (curr_bus, curr_time) = curr
    if nxt_time < curr_time:
        return nxt
    return curr

desired = functools.reduce(selection, avail.items())
(bus, arrival_time) = desired
print("one")
print(bus * (arrival_time - time))
