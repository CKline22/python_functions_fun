def name_args(**kwargs) :
    for i in kwargs.keys():
        print(f"{i}:{kwargs[i]}")
name_args(name="Jack", location="Ohio")

def all_true(iter):
    return all(iter)
print(all_true([True,True,True]))
print(all_true((True,False)))

def one_true(iter):
    return any(iter)
print(one_true([True,True,True]))
print(one_true([False, False, False]))
print(one_true((True, False)))

def recursive_factorial(i):
    if i <= 1:
        return 1
    else:
        return i * recursive_factorial(i-1)
print(recursive_factorial(5))
print(recursive_factorial(9))    


