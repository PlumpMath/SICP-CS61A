def sum_squares(N):
    """The sum of K**2
    for 1 <= K <= N."""
    def part_sum(k, accum):
        if k <= N:
            return part_sum(k+1, accum + k**2)
        else:
            return accum
    return part_sum(1, 0)
print(sum_squares(3))

########################################
def find_first(start, pred):
    """Find the smallest k >= START such that PRED(START)."""
    if pred(start):
        return start
    else:
        return find_first(start+1, pred)

def pred(x):
    return x * x == 16
print(find_first(2,pred))

#########################################
import sys
sin60 = 3**0.5 / 2
def make_gasket(x, y, s, n, output):
    """Write Postscript code for a Sierpinski鈥檚 gasket of order N
    with lower-left corner at (X, Y) and side S on OUTPUT."""
    if n == 0:
        draw_solid_triangle(x, y, s, output)
    else:
        make_gasket(x, y, s/2, n - 1, output)
        make_gasket(x + s/2, y, s/2, n - 1, output)
        make_gasket(x + s/4, y + sin60*s/2, s/2, n - 1, output)
def draw_solid_triangle(x, y, s, output):
    "Draw a solid triangle lower-left corner at (X, Y) and side S."
    print("{0} {1} moveto " # Go x, y
    "{2} 0 rlineto " # Horizontal move by s units
    "-{3} {4} rlineto " # Move up and to left
    "closepath fill" # Close path and fill with black
    .format(x, y, s, s/2, s*sin60), file=output)

def draw_gasket(n, output=sys.stdout):
    print("%!", file=output)
    make_gasket(100, 100, 400, 8, output)
    print("showpage", file=output)


draw_gasket(1)
