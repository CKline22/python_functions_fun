
def print_everything (*names):
    for i in names:
        print(i)
print_everything("jack", "sam", "frank")

def inner_func (a,b):
    def inner_1():
        return a+b
    def inner_2():
        return a-b
    print(inner_1()+inner_2())

def lunch_lady (name, lunch="mystery meat"):
    print(name, lunch)

def sum_n_product(x=10,y=5):
    value_1 = x + y
    value_2 = x * y
    return value_1, value_2

alias_arb_args = print_everything

def arb_mean(*args):
  total = 0
  for a in args:
    total += a
  print(a/len(args))

def arb_longest_string(*args):
  long = 0
  longest = ""
  for a in args:
    if len(a) > long:
      long = len(a)
      longest = a
  return longest