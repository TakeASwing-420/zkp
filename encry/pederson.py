import random
from functools import reduce
from py_ecc.bn128 import G1, add, eq, field_modulus, multiply

x, y = random.randint(1, field_modulus - 1), random.randint(1, field_modulus - 1)
G, B = multiply(G1, x), multiply(G1, y)

def commit(secret, salt):
    return add(multiply(G, secret), multiply(B, salt))

# Let's say polynomial be f(x) = x^2 + 2x + 3
salts = [random.randint(1, field_modulus - 1) for _ in range(3)]
u = random.randint(1, field_modulus - 1)
C0, C1, C2 = commit(3, salts[0]), commit(2, salts[1]), commit(1, salts[2])
commitments = [C0, C1, C2]
y, pie = u**2 + 2*u + 3, salts[2]*u**2 + salts[1]*u + salts[0]

def verify(commitments, y, pie):
    u_powers = [u**i for i in range(len(commitments))]
    combined_commitment = reduce(add, [multiply(commitments[i], u_powers[i]) for i in range(len(commitments))])
    commitment_to_y_pie = commit(y, pie)
    return eq(combined_commitment, commitment_to_y_pie)

is_valid = verify(commitments, y, pie)
print("Verification result:", is_valid)
