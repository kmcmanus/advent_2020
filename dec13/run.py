import math
import functools
import itertools
from signal import signal, SIGINT
from sys import exit

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

def make_generator(shift, step, start):
    start = math.ceil(start / step) * step
    return (
        i - shift
        for i in itertools.count(start, step=step)
    )
start_at = 100000000000000
with open('input', 'r') as f:
    f.readline()
    busses = [
        make_generator(i, int(line.strip()), start_at)
        for i, line in enumerate(f.readline().split(","))
        if 'x' not in line
    ]

print(busses)

lmax = 0
def handler(signal_received, frame):
    global lmax
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    print(lmax)
    exit(0)

signal(SIGINT, handler)
def intersection(left, right):
    global lmax
    l_val = left.__next__()
    r_val = right.__next__()
    while True:
        while l_val < r_val:
            l_val = left.__next__()
        while r_val < l_val:
            r_val = right.__next__()
        if l_val == r_val:
            lmax = max(lmax, l_val)
            yield l_val
            l_val = left.__next__()
            r_val = right.__next__()

final = functools.reduce(intersection, busses)
print("two")
print(final.__next__())
