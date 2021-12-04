def problem1(n):
  multiples = []
  i = 3
  while i < n:
    multiples.append(i)
    i += 3
  i = 5
  while i < n:
    multiples.append(i)
    i += 5
  return sum(set(multiples))

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

def problem4(n):
  start_num = int("9" * n) ** 2
  end_num = int("9" * (n - 1)) ** 2 + 1
  while start_num >= end_num:
    str_num = str(start_num)
    if str_num[:n] == str_num[:n - 1:-1]:
      for x in range(100, 1000):
        if start_num % x == 0 and 1000 > start_num // x > 100:
          return start_num
    start_num -= 1

def problem5(n):
  num = n
  numbers = range(int(n // 2, n))
  while True:
    for x in numbers:
      if num % x != 0:
        break
    else:
      return num
    num += n
    
def problem6(n):
  return sum(range(n + 1)) ** 2 - sum(x ** 2 for x in range(n + 1))

def problem7(n):
    limitn = 10000000+1
    not_prime = [False] * limitn
    primes = 0
    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in range(i*2, limitn, i):
            not_prime[f] = True
        
        primes += 1
        if primes == n:
          return i

if __name__ == "__main__":
  print(problem1(1000))
  print(problem2(4000000))
  print(problem3(600851475143))
  print(problem4(3))
  print(problem5(20))
  
