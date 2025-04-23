import math
num = float(input("Enter a number: "))

if num > 0:
    sqrt_val = math.sqrt(num)
    log_val = math.log(num)
else:
    sqrt_val = "Undefined (number must be >= 0)"
    log_val = "Undefined (number must be > 0)"

sin_val = math.sin(num)

print("\nResults:")
print(f"Square root: {sqrt_val}")
print(f"Natural logarithm: {log_val}")
print(f"Sine (in radians): {sin_val}")
