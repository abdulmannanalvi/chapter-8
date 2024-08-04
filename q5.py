def sum_natural_numbers(num):

  if num == 0:
    return 0
  else:
    return num + sum_natural_numbers(num - 1)

# Example usage:
num = 5
result = sum_natural_numbers(num)
print(f"The sum of the first {num} natural numbers is: {result}")
