def problem2(n):
  total = 0
  x = 1
  y = 1
  while x <= n:
    if x % 2 == 0:
      total += x
    x += y
    y = x - y
  return total

if __name__ == "__main__":
  print(problem2(4000000))