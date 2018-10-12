import math

# Enter two equations

e1 = lambda x: x+6.05
e2 = lambda x: 2*x**2

# Range

MIN = 2
MAX = 3
STEP = 200 # How many steps within each int?

last_diff = diff = None
last_closer = closer = None

for x in range(MIN, MAX+1):
    for s in range(STEP):
        xs = x + s/STEP
        y1 = e1(xs)
        y2 = e2(xs)
        if diff: last_diff = diff
        diff = abs(y1-y2)
        if closer is not None: last_closer = closer
        closer = (last_diff and last_diff > diff)
        missed = (not closer and last_closer)
        
        match = (y1 == y2)
        data = "x: {:8.4}  y1: {:8.4}  y2: {:8.4}  diff: {:8.4}".format(xs, y1, y2, diff)
        print("MATCH" if match else "     ",
              data,
              " closer" if not(match) and closer else "",
              " MISSED?!" if missed else ""
              )
