def mean(number):
  string = str(number)
  total = 0
  for n in string:
    total += int(n)
    count = len(string)
  return total/count
print(mean(12345))

