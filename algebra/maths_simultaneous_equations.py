import math

# Enter two equations

e1 = lambda x: math.sqrt(25-x**2)

e2 = lambda x: (10-x)/2
def e2(x): return (10-x)/2

# Range

MIN = 0
MAX = 5
STEP = 10 # How many steps within each int?

last_diff = diff = None
for x in range(MIN, MAX+1):
    for s in range(STEP):
        xs = x + s/STEP
        y1 = e1(xs)
        y2 = e2(xs)
        if diff:
            last_diff = diff
        diff = abs(y1-y2)
        closer = (last_diff and last_diff > diff)
        
        match = (y1 == y2)
        print("MATCH" if match else "     ",
              "x:", xs, "y1:", y1, "y2:", y2,
              diff,
              "closer" if not(match) and closer else ""
              )
