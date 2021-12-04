def problem3(n):
  factors = []
  for i in range(1, int((n) ** 0.5)):
    if n % i == 0:
      for j in range(2, int((i))):
        if i % j == 0:
          break
      else:
        factors.append(i)
      for j in range(2, int((n / i))):
        if (n / i) % j == 0:
          break
      else:
        factors.append(int(n / i))
  return(max(factors))

if __name__ == "__main__":
  print(problem3(600851475143))