def problem5(n):
  num = 1
  while True:
    for x in range(int(n / 2), n):
      if num % x != 0:
        break
    else:
      return num
    num += 1

print(problem5(20))