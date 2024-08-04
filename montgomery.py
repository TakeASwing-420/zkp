import time
from numpy import int64

# Define a simple point addition and doubling functions
def point_add(P, Q, a, p):
    # This is a placeholder for point addition
    if P == Q:
        return point_double(P, a, p)
    # Simplified addition logic (not secure or accurate for real ECC)
    x1, y1 = P
    x2, y2 = Q
    lam = (y2 - y1) * pow(x2 - x1, -1, p) % p
    x3 = (lam ** 2 - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p
    return (x3, y3)

def point_double(P, a, p):
    # This is a placeholder for point doubling
    x, y = P
    lam = (3 * x ** 2 + a) * pow(2 * y, -1, p) % p
    x3 = (lam ** 2 - 2 * x) % p
    y3 = (lam * (x - x3) - y) % p
    return (x3, y3)

def monto(k: int, P, a, p) -> int64:
    R0 = (0, 0)  # Identity element
    R1 = P

    # Convert the scalar k to a binary string
    bits = bin(k)[2:]

    for bit in bits:
        if bit == '0':
            R1 = point_add(R0, R1, a, p)
            R0 = point_double(R0, a, p)
        else:
            R0 = point_add(R0, R1, a, p)
            R1 = point_double(R1, a, p)

    return R0

# Example elliptic curve parameters (using simple numbers for illustration)
a = 2
p = 97  # Prime number
P = (3, 6)  # Base point

# Example scalar
k = 123456

# Measure the execution time
start_time = time.time()
result = monto(k, P, a, p)
end_time = time.time()

execution_time = end_time - start_time

print(f"Result: {result}")
print(f"Execution Time: {execution_time} seconds")
