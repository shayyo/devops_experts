
first = 7
second = 44.3


print(first + second)
print(first * second)
print(first / second)

print("=" * 20)


a = 8
a = 17
a = 9
b = 6
c = a + b
b = c + a
b = 8
# since Python is dynamically typed language, variables can be declared and then changed later in the code
# a=9, b=8, c=15
print(a, b, c)

print("=" * 20)

# according tp Python documentation there is no real difference between single ('') and double ("") quotes
name = "john"
name = 'john'

print("=" * 20)

# The issue with "print("result is: " + my_number)" is that string and integer cannot be concatenated
# using '+' sign since '+' sign evaluates the entire expression as a whole before returning it
my_number = 5+5
# a the correct way to concatenate string and integer is by using ','
print("result is: ", my_number)

print("=" * 20)

x = 5
y = 2.36
print(x + int(y))  # output is '7'

print("=" * 20)

x = 17
y = 55

if x > y:
    print("BIG")
elif x < y:
    print("small")


print("=" * 20)

s = 3

if s == 1:
    print("summer")
elif s == 2:
    print("winter")
elif s == 3:
    print("fall")
else:
    print("spring")

print("=" * 20)

a = 8
b = "123"
print(a, b)
print(a + int(b))

