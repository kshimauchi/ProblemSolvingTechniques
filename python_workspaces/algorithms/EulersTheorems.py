
# Euler's Theorem: if gcd(a, n)=1:
# Find e, d, n that for all m in Z(n) where z(n) is the integers in modulo n
# a^(Totient(n))= 1 mod n
# ed-1 = Totient
# number of positive integer less than n that are relatively prime
# A simple method to evaluate
# Euler Totient Function
def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)

def phi(n):
    result = 1
    for i in range(2, n):
        if (gcd(i, n) == 1):
            result += 1
    return result

for n in range(1, pow(2,666)):
    print("phi(",n,") = ",
           phi(n), sep = "")