# Author: Paul Quaife
# Date: 3/4/2021
# Description: Reverses list of numbers given.

def reverse_list(vals):
    """Def reverses list given."""
    i = 0
    j = len(vals)-1
    while i < j:
        tmp = vals[i]
        vals[i] = vals[j]
        vals[j] = tmp
        i += 1
        j -= 1
