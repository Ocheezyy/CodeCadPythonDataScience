def coffee_bot():
  print('Welcome to the cafe!')
  size = get_size()
  drink_type = get_drink_type()
  if drink_type == 'Latte':
    latte_type = order_latte()
  #latte_type = order_latte()
  print("Alright, that's a {} {}!".format(size, drink_type))
  name = order_name()
  print(f"Thanks, {name}! Your drink will be ready shortly.")
  
def get_size():
  res = input('What size drink can i get for you? \n[a] Small\n[b] Medium\n[c] Large \n> ')
  if (res == 'a'):
    return 'Small'
  elif (res == 'b'):
    return 'Medium'
  elif (res == 'c'):
    return 'Large'
  else:
    return "I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response"
def get_drink_type():
  res = input("What type of drink would you like?\n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n>")
  if res == 'a':
    return 'Brewed Coffee'
  elif res == 'b':
    return 'Mocha'
  elif res == 'c':
    order_latte()
  else:
    return "I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response."
def order_latte():
  res = input("And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk")
  if res == 'a':
    return '2% milk'
  elif res == 'b':
    return 'Non-fat milk'
  elif res == 'c':
    return 'Soy milk'
  else:
    return "I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response."
def order_name():
  res = input("Can I get your name please?\n>")
  return res
  
coffee_bot()