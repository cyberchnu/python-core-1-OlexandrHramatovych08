def mean(number):
  string = str(number)
  total = 0
  for n in string:
    total += int(n)
    count = string.count(n)
  return total/count


