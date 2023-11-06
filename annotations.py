def increment(n: int) -> int:
    return n + 1


print(increment(5))

count: int = 0


# exceptions
try:
    result = 2 / 0
except ZeroDivisionError:
    print('Cannot divide by zero!')
finally:
    result = 1
print(result)

try:
    raise Exception('AN ERROR!')
except Exception as error:
    print(error)


class DogNotFoundException(Exception):
    print("inside")
    pass


try:
    raise DogNotFoundException()
except DogNotFoundException:
    print('dog not found!')

# with statement
filepath = 'C:/Users/pedro/test.tsx'
# auto close file
with open(filepath, 'r') as file:
    content = file.read()
    print(content)