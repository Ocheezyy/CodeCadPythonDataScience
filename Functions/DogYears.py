def dog_years(name, age):
  dogage = age * 7
  return name + ", you are " + str(dogage) + " years old in dog years"

print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"
#hello