def gcd(a, b):

    if a > b:
        a, b = b, a

    if b % a == 0:
        return a
    else:
        return gcd(b%a, b)

print(gcd(20, 15))

def prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print(prime(19))
print(prime(20))