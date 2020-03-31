#problem 1
print("\nProblem 1\n")
def append_sum(lst):
    lst.append(lst[-1] + lst[-2])
    lst.append(lst[-1] + lst[-2])
    lst.append(lst[-1] + lst[-2])
    return lst


print(append_sum([1, 1, 2]))


# problem 2
print("\nProblem 2\n")
def larger_list(lst1, lst2):
    lst1len = len(lst1)
    lst2len = len(lst2)
    if lst1len > lst2len:
        return lst1[-1]
    if lst2len > lst1len:
        return lst2[-1]
    if lst1len == lst2len:
        return lst1[-1]
    else:
        return "No list"

print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

#problem 3
print("\nProblem 3\n")
def more_than_n(lst, item, n):
    lstcount = lst.count(item)
    if lstcount > n:
        return True
    else:
        return False

print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))


#problem 4 
print("\nProblem 4\n")
def append_size(lst):
    lst.append(len(lst))
    return  lst

#problem 5
print("\nProblem 5\n")
def combine_sort(lst1, lst2):
    lst12 = lst1 + lst2
    lst12.sort()
    return lst12