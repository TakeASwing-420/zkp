# @dev This code computes the inverse of a number mod p, and uses it to compute a/b mod p
#The general way to compute a “fraction” in a finite field is the numerator times the multiplicative inverse of the denominator, modulo p:


def compute_field_element_from_fraction(num, den, p):
  inv_den = pow(den, -1, p)
  return (num * inv_den) % p

'''
It is not possible to do this when the denominator is a multiple of p. For example, 1/7 cannot be represented in the finite field p = 7 because pow(7, -1, 7) has no solution. The modulo is taking the remainder after division, and the remainder of 7/7 is zero, or more generally, 7/d is zero when d is a multiple of 7. The multiplicative inverse means we can multiply a number and its inverse together to get 1, but if one of the numbers is zero, there is nothing we can multiply by zero to get 1
'''
arr = [(3, 7, 7), (12, -1, 4), (2, 5, 3), (11,6,23)]

for a, b, c in arr:
  print()
  try:
    res = compute_field_element_from_fraction(a, b, c)
    print(res)
  except Exception as e:
    print(f"error occurred: {str(e)}")
  