import random
from functools import reduce
from py_ecc.bn128 import G1, add, eq, field_modulus, multiply
# WARNING: Points are generated in this manner for convenience. In practice, the point's (x, y) value must be selected randomly and the discrete logs should never be known to anyone.
g, b = random.randint(1,field_modulus - 1), random.randint(1,field_modulus - 1)
G, B = multiply(G1, g), multiply(G1, b)
def commit(secret, salt):
    return add(multiply(G, secret), multiply(B, salt))

# Let's say polynomial be f(x) = x^2 + 2x + 3
salts = [random.randint(1, 10**9 + 7) for _ in range(3)]
C0, C1, C2 = commit(3, salts[0]), commit(2, salts[1]), commit(1, salts[2])
commitments = [C0, C1, C2]
u = random.randint(1, 10**9 + 7)  # verifier receives the commitments and responds with u
y, pi = u**2 + 2 * u + 3, salts[2] * u**2 + salts[1] * u + salts[0]  # prover computes the value of y and pi and sends it to verifier

def verify(commitments, y, pi):
    u_powers = [u**i for i in range(len(commitments))]
    combined_commitment = reduce(add, [
        multiply(commitments[i], u_powers[i]) for i in range(len(commitments))
    ])
    commitment_to_y_pi = commit(y, pi)
    return eq(combined_commitment, commitment_to_y_pi)
    
is_valid = verify(commitments, y, pi)
print("Verification result:", is_valid)
