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

def rev_string(str):
    return str[::-1]

print(rev_string(""))
print(rev_string("meat"))


def num_within(x, a, b):
    return x in range(a, b+1)

print(num_within(12,24,36))
print(num_within(12,15,12))


triangle = [[1],[1,1]]
def pascal(i):
    if i < 1:
        print("not a number of rows")
    elif i == 1:
        print(triangle[0])
    else:
        row_num = 2
        while len(triangle) < i:
            row = []
            row_previous = triangle[row_num - 1]
            length = len(row_previous) + 1
            for e in range(length):
                if e == 0:
                    row.append(1)  
                elif e > 0 and e < length - 1:
                    row.append(triangle[row_num-1][e-1]+ triangle[row_num - 1][e])
                else:
                    row.append(1)
            triangle.append(row)
            row_num += 1

        for row in triangle:
            print(row)

pascal(6)
pascal(10)
