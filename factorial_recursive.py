def fact(num):
  if num == 1:
    return 1
  return num * fact(num - 1)

fact(5)
