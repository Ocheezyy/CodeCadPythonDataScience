def lots_of_math(a, b, c, d):
  ab = a + b
  cd = d - c
  abcd = ab * cd
  print(ab)
  print(cd)
  print(abcd)
  return abcd % a

print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0