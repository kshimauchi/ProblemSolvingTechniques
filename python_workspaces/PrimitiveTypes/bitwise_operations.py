# Does a "bitwise and". Each bit of the output is 1 if the
# corresponding bit of x AND of y is 1, otherwise it's 0.
print(6&12)     #4
print(2&2)      #2
print(1&2)      #0
print(10&10)    #10
print(5&5)      #5
print(1&1)      #1

# Does a "bitwise or". Each bit of the output is 0 if the
# corresponding bit of x AND of y is 0, otherwise it's 1.
print(1|2)

# Returns x with the bits shifted to the right by y places.
# This is the same as //'ing x by 2**y.
print(8>>1)

# Returns x with the bits shifted to the right by y places.
# This is the same as //'ing x by 2**y.
print(-16>>2)

# Returns x with the bits shifted to the left by y places
# (and new bits on the right-hand-side are zeros). This
# is the same as multiplying x by 2**y.
print(1<<10)
print(10000000101 << 2&1)

# Returns the complement of x - the number you get by switching
# each 1 for a 0 and each 0 for a 1. This is the same as -x - 1.
print(~0)

# Floor division - division that results into whole number
# adjusted to the left in the number line
print(2//1)