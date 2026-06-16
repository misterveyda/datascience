a, b = 17, 5
print(a / b)    # 3.4   — always returns float
print(a // b)   # 3     — floor division (rounds down)
print(a % b)    # 2     — remainder (useful for even/odd check)
print(a ** b)   # 1419857  — 17 to the power 5
 
# Check if n is even
n = 42
print(n % 2 == 0)    # True
 
# Augmented assignment operators
x = 10
x += 5     # x = 15   (same as x = x + 5)
x -= 3     # x = 12
x *= 2     # x = 24
x //= 5    # x = 4
x **= 3    # x = 64
