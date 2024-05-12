def ExF(n):
  if n == 1:
      return 2
  elif n == 2:
      return 5
  else:
      return ExF(n - 1) * ExF(n - 2)

resultado = ExF(6)
print(resultado)