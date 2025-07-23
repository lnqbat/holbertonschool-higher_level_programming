# Python - Everything is Object

## Introduction

This project explains a core concept of Python: **everything is an object**. Understanding object identity and mutability is essential for writing safe and efficient code in Python.

---

## `id` and `type`

Every object in Python has:
- a unique identifier, given by `id`
- a type, given by `type`

**Example:**
```
a = 5
print(type(a))  # <class 'int'>
print(id(a))    # Example output: 9780960 
```
## Mutable Objects
Mutable objects can be modified after creation. Lists, dictionaries, and sets are mutable.

**Example:**
```
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)  # Output: [1, 2, 3, 4]
```

## Immutable Objects
Immutable objects cannot be changed after creation. Integers, strings, and tuples are immutable.

**Example:**
```
a = 10
b = a
a = a + 1
print(b)  # Output: 10
```

## Why does it matter?
Mutable: Changes can affect all variables pointing to the same object.

Immutable: Changes create a new object, so other variables remain unchanged.

## Arguments passed to functions
Passing a mutable object (e.g., a list): the function can modify the original object.

Passing an immutable object (e.g., an int): the function cannot change the original.

**Example:**
```
def add_item(lst):
    lst.append(99)

my_list = [1, 2, 3]
add_item(my_list)
print(my_list)  # [1, 2, 3, 99]
```
```
def increment(n):
    n += 1

a = 5
increment(a)
print(a)  # 5
```
## Conclusion
Understanding the difference between mutable and immutable objects,  and avoiding subtle bugs related to object references and data manipulation.

