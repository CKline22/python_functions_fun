def max_number(a,b,c):
    return max([a,b,c])
print(max_number(2,4,6))
print(max_number(25,50,75))

def mult_list(list):
    if len(list) == 0:
        return 0
    product = list[0]

    if len(list) > 1:
        for i in list[1:]:
            product = product * i
    return product

print(mult_list([2,4,6]))
print(mult_list([25,50]))                