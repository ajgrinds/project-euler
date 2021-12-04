def problem5(n):
  num = 0
  while True:
    for x in range(n):
      if num % x != 0:
        break
    else:
      print(num)
    num += 1

problem5(10)