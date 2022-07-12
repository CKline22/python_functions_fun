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

def recursive_deduplicate(my_str, i=0):
    if len(my_str) <= 1 or i == len(my_str)-1:
        return my_str
    else:
        if my_str[i] == my_str[i+1]:
            return
        recursive_deduplicate(my_str[0:i]+my_str[i+1:], i)
        else:
            return recursive_deduplicate(my_str, i+1)                  
print(recursive_deduplicate("aaaa"))
print(recursive_deduplicate("aaba"))
print(recursive_deduplicate("apple"))
print(recursive_deduplicate(""))                    

def recursive_reverse(str, i=0):
    if len(str)==0:
        return ""
    elif i == len(str)-1:
        return str[0]
    else:
        return str[-1-i] + recursive_reverse(str, i+1)

print(recursive_reverse("aaaa"))
print(recursive_reverse("aaba"))
print(recursive_reverse("apple"))
print(recursive_reverse(""))               

