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

if __name__ == "__main__":
  print(problem1(1000))