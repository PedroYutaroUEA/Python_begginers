from functools import reduce

lambda num: num * 2

mul = lambda a, b: a * b

print(mul(5, 3))

# map
numbers = [1, 2, 3, 4, 5]


def double(n):
    return n*2


result = list(map(double, numbers))
print(result)

nums = [2, 4, 6, 8, 10]

res = list(map(lambda n: n * 3, nums))
print(res)

# filter
numbers = [0, 1, 2, 3, 4, 5]
result = list(filter(lambda n: n % 2 == 0, numbers))

print(result)

# reduce
expenses = [
    ('Dinner', 80),
    ('Car repair', 120)
]
sum_ex = 0
for ex in expenses:
    sum_ex += ex[1]
print(sum_ex)

expenses = [
    ('Dinner', 80),
    ('Car repair', 120),
]

sum_ex = reduce(lambda a, b: a[1] + b[1], expenses)
print(sum_ex)

# recursion


def factorial(n):
    if n == 1: return 1
    return n * factorial(n - 1)


print(factorial(4))

# decorators: A decorator is a design pattern in Python that allows a user to add new functionality to an existing
# object without modifying its structure. Decorators are usually called before the definition of a function you want to
# decorate.


def logtime(fun):
    def wrapper():
        print("before")
        val = fun()
        print("after")
        return val
    return wrapper


@logtime
def hello():
    print('hello')

hello()