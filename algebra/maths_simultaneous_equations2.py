import math

# Enter two equations

e1 = lambda x: math.sqrt(25-x**2)
e2 = lambda x: 2 + (10-x)/2

# Range

MIN = 0
MAX = 5
STEP = 2 # How many steps within each int?

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
        print("MATCH" if match else "     ",
              xs, y1, y2,
              diff,
              "closer" if not(match) and closer else "",
              "MISSED?!" if missed else ""
              )
