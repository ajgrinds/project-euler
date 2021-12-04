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

if __name__ == "__main__":
  print(problem4(3))

