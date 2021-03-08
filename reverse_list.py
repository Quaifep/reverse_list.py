# Author: Paul Quaife
# Date: 3/4/2021
# Description: Reverses list of numbers given.

def reverse_list(vals):
    """Def reverses list given."""
    x = 0
    y = len(vals)-1
    while x < y:
        tmp = vals[x]
        vals[x] = vals[y]
        vals[y] = tmp
        x += 1
        y -= 1
