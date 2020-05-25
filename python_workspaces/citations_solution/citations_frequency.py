# Problem Solving in python 3.8 Interpreter
# Problem:
# h-index is a metric that measures both the productivity and citaitons impact of a x, the x h-index is the largest
# number h such that, the researcher has published h papers that have each been cited at least h times
# if x published papers A, B, C, D, E, F, G, H, I which have been cited [1,4,1,4,2,1,3,5,6] times respectively,
# then x's h-index is 4.
# To find h-index suppose you create a variable x which starts 1, and begins to increment with each comparison,
# as soon as count is equal (may or may not be sorted) and are allowed to modify it.
# how many entries in the array are greater than or equal to the count?
# As soon as the count is greater or equal to the number of entries than the count, the h-index is 1 less than the count.
from typing import List

citations =[1,1,1,2,3,4,4,5,6]
def h_index(citations: List[int])-> int:
    citations.sort()            # sort(): internally is O(n lg n)
    n = len(citations)          # len(
    for i, c in enumerate(citations):
        if c >= n - i:
            return n - i
    return 0
print(h_index(citations))


