arbol = int(input())
i = 1

while i <= arbol:
  print(" " * (arbol - i) + "*" * (i * 2 - 1))
  i += 1
  