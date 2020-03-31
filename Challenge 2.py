#problem 1
print("\nProblem 1\n")
def every_three_nums(start):
  return list(range(start, 101, 3))

print(every_three_nums(91))

#problem 2
print("\nProblem 2\n")
def remove_middle(lst, start, end):
    del lst[start:end+1]
    return lst

print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

#problem 3
print("\nProblem 3\n")
def more_frequent_item(lst, item1, item2):
    item1ct = lst.count(item1)
    item2ct = lst.count(item2)
    if item1ct > item2ct:
        return item1
    if item2ct > item1ct:
        return item2
    else: 
        return item1

print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

#problem 4
print("\nProblem 4\n")

def double_index(lst, index):
  # Checks to see if index is too big
  if index >= len(lst):
    return lst
  else:
    # Gets the original list up to index
    new_lst = lst[0:index]
 # Adds double the value at index to the new list 
  new_lst.append(lst[index]*2)
  #  Adds the rest of the original list
  new_lst = new_lst + lst[index+1:]
  return new_lst

print(double_index([3, 8, -10, 12], 2))

#problem 5
print("\nProblem 5\n")
def middle_element(lst):
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
    return sum / 2
  else:
    return lst[int(len(lst)/2)]

print(middle_element([5, 2, -10, -4, 4, 5]))