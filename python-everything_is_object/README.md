# Python Internals: Assignment, Mutables, Immutables, Aliases, and Small Integer Magic

## Introduction

In Python, **everything is an object**. But understanding how assignment works, how objects are stored and referenced in memory, the distinction between mutable and immutable types, the concept of aliasing, and internal optimizations like small integer pre-allocation is key to mastering Python programming. This document covers all these aspects, with concrete examples and memory schemas.

---

## 0. `id` and `type`

Every object in Python has:
- a unique identifier, given by `id`
- a type, given by `type`

**Example:**
```
a = 5
print(type(a))  # <class 'int'>
print(id(a))    # Example output: 9780960 
```

## 1. Mutable Objects

**Mutable objects** can be changed after their creation. Modifying a mutable object affects all references (aliases) to it, because the object itself in memory is updated.

**Common mutable types:**  
- `list`
- `dict`
- `set`

**Example:**
```python
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)    # Output: [1, 2, 3, 4]
```
**Memory schema:**
```
l1 ──► [1, 2, 3, 4] ◄── l2
```

---

## 2. Immutable Objects

**Immutable objects** cannot be changed after their creation. Any operation that seems to "modify" them creates a new object.

**Common immutable types:**  
- `int`
- `str`
- `tuple`
- `frozenset`

**Example:**
```python
x = 10
y = x
x = x + 1
print(y)  # Output: 10
```
**Memory schema:**
```
Before:  x ──► 10 ◄── y
After:   x ──► 11
          y ──► 10
```

---

## 3. Assignment vs. Referencing

In Python, **assignment** does not copy objects. It only creates a new reference (an alias) to the existing object.

**Example:**
```python
a = [1, 2, 3]
b = a
b.append(42)
print(a)  # [1, 2, 3, 42]
```
**Memory schema:**
```
a ──► [1, 2, 3, 42] ◄── b
```
**Modifying** the object via one reference changes it for all aliases.

---

## 4. Memory Schemas: Examples

**Example 1: List aliasing (mutable)**
```python
l1 = [1, 2]
l2 = l1
l1.append(3)
```
```
l1 ──► [1, 2, 3] ◄── l2
```

**Example 2: String immutability**
```python
s1 = "hello"
s2 = s1
s1 += " world"
```
```
Before: s1 ──► "hello" ◄── s2
After:  s1 ──► "hello world"
         s2 ──► "hello"
```

---

## 5. How Variable Values Are Managed When Passing to a Function

When you pass a variable to a function, the **reference** to the object is passed.  
- For **mutable** objects: the function can modify the original object.
- For **immutable** objects: the function cannot change the original; a new object is created if modified.

**Mutable example:**
```python
def mutate(l):
    l.append(99)

a = [1, 2, 3]
mutate(a)
print(a)  # Output: [1, 2, 3, 99]
```
**Immutable example:**
```python
def increment(n):
    n += 1

b = 5
increment(b)
print(b)  # Output: 5
```

---

## 6. Integer Pre-allocation in CPython (`NSMALLPOSINTS`, `NSMALLNEGINTS`)

CPython pre-allocates all integers in the range `-5` to `256` at startup.  
- These objects are shared throughout the program for efficiency.

**Example:**
```python
a = 100
b = 100
print(a is b)  # True

c = 1000
d = 1000
print(c is d)  # False
```
**Why?**  
- Small integers are heavily used (indices, counters, etc.).
- Pre-allocating saves memory and improves speed.

---

## 7. The Mechanism of Aliases

When two or more variables refer to the same object, they are called **aliases**.

**Example:**
```python
x = [42]
y = x
y.append(99)
print(x)  # Output: [42, 99]
```
Both `x` and `y` are aliases for the same list.

---

## 8. How `NSMALLPOSINTS` and `NSMALLNEGINTS` Are Used

- `NSMALLPOSINTS` and `NSMALLNEGINTS` are internal CPython constants.
- When Python starts, it creates and stores objects for integers from `-5` to `256`.
- Any use of an integer in this range will point to the same, shared object.

---

## 9. Why These Values?

The range (`-5` to `256`) is chosen based on common usage:
- Negative: Only a few negative integers are used frequently (e.g., `-1`).
- Positive: Many small positive integers are used in loops, ranges, etc.
- Sharing these saves memory and boosts performance.

---

## 10. Special Case: Tuple and Frozen Set

- **Tuples** and **frozensets** are immutable containers, but they can contain **mutable** objects.
- If a mutable object inside a tuple or frozenset is modified, the content of the container appears to change.

**Example:**
```python
l = [1, 2]
t = (l, 3)
l.append(4)
print(t)  # Output: ([1, 2, 4], 3)
```
The tuple itself is immutable, but its elements may be mutable objects.

---

## Conclusion

Understanding assignment, mutability, memory models, aliasing, small integer pre-allocation, and container behaviors is essential for writing robust and efficient Python code.  
