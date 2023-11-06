from enum import Enum

name = "pedro"
print(type(name))
print(name is str)
print(isinstance(name, int))


# Ternary operation


def is_adult(age):
    return "is adult" if age >= 18 else "is kid"


print(is_adult(int(12)))

print(""""
EU SOU

MAIS LOUCO

DO  QUE TODOS
    VOCES
""")

print(len(name))
print("edr" in name)

print("Ped\"ro")
print(name[0], name[-1], name[1:3])

# booleans

book_1 = True
book_2 = False

read_any_book = any([book_1, book_2])
print(read_any_book)
ready_all = all([book_1, book_2])
print(ready_all)

# numbers
print(2 + 3j)
num = complex(2, 3)
print(num.real, num.imag)

print(abs(-5.125))
print(round(-5.7525, 1))


class State(Enum):
    INACTIVE = 0
    ACTIVE = 1


print(list(State))
print(State.ACTIVE.value)
print(State(1))

# lists

items = ["Roger", 1, "maria", True, 12]
items[2] = "jose"
print(items)
print(items[:3])
items.append("judeu")
items.extend("palestino")

new_items = ['gore', 100, False, "bolsonaro"]
items += new_items

print(items)

items.remove("gore")
print(items)

print(items.pop())
print(items)

items.insert(2, 'maria')
print(items)

items[1:1] = ['test1', 'test2']
print(items)

str_list = ['jesus', 'francisco', 'Niko', 'yutaro', 'raphael']
copy_list = sorted(str_list, key=str.lower)
str_list.sort()
print(str_list)
print(copy_list)

# tuples

names = ("Pedro", "Joao", "Maria", "ricardo", "juliana")
print(names)
print(names[-1])
print(sorted(names))

new_tuple = names + ("Tina", "Yasmin")
print(new_tuple)

# dictionaries

dic = {
    "name": "Pedro",
    "isAdmin": False,
    "age": 19,
    "color": "green"
}
dic_cp = dic.copy()
dic["name"] = "Zoink"
print(dic)
print(dic.keys())
print(dic.values())
print(dic.get("age"))
print(dic.get("color", "black"))

print(dic.pop("name"))
print(dic)
print(dic.popitem())
print(dic)

dic["new user"] = "Yutaro"
del dic["age"]
print(dic)
print(dic_cp)

# sets

set1 = {"rick", "davy", "hugo", "rick"}
set2 = {"pedro", "rick", "joseph"}

intersect = set1 & set2
mod = set1 | set2
diff = set1 - set2
ft = set1 > set2
print(intersect)
print(mod)
print(diff)
print(ft)
print(list(set1))

# functions


def change(v):
    v["name"] = "pedro"


val = {"name": "beaul"}
change(val)

print(val)


def hello(name):
    if not name:
        return 'set a name you son of a b---'
    print(f"hello {name}")


hello("Pedro")
hello(False)
print(hello(False))


def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(' ')
    for word in words:
        say(word)


talk('I am going to brazil')


def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


incrementor = counter()
print(incrementor())
print(incrementor())
print(incrementor())

# loops

items = [10, 20, 30, 40]

for item in items:
    if item == 20:
        continue
    print(item)