# Greatest Common Denominator
# Recall Definition:
# gcd(a, 0) = |a|, for a ≠ 0,
# since any number is a divisor of 0,
# and the greatest divisor of a is |a|.
# This is usually used as the base case in the Euclidean algorithm.
# If a divides the product b⋅c, and gcd(a, b) = d, then a/d divides c.
# If m is a non-negative integer, then gcd(m⋅a, m⋅b) = m⋅gcd(a, b).
def computeGreatestCommonDenominator(dividend, divisor):
    if dividend > divisor:
        remainder = divisor
    else:
        remainder = dividend
    for i in range(1, remainder + 1):
        if((dividend % i ==0) and (divisor % i ==0)):
            gcd =i
    return gcd
#print(computeGreatestCommonDenominator(60,48)) #12
#print(computeGreatestCommonDenominator(777, 7))

# gcd
def gcd(dividend, divisor):
    if(divisor == 0):
        return dividend
    else:
        return gcd(divisor, dividend % divisor)
#print(gcd(60,64))

# gcd
def computeGCD(dividend, divisor):
    while(divisor):
        dividend, divisor = divisor, dividend % divisor
        return dividend
#print(computeGCD(234, 12))