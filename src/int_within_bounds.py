def int_within_bounds(number, lower_bound, upper_bound):
  if number >= lower_bound and number < upper_bound and type(number)==int:
    return True
  else:
    return False
