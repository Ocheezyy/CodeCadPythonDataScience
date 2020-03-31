def tip(total, percentage):
  percentage = percentage / 100
  amt = total * percentage 
  return amt

print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0