# test

lists = [1, 3, 2]

print sorted(lists)
print lists

print lists.reverse()

print len(lists)

for i in lists:
    print i
    print "hello" + str(i)

for i in range(1, 10, 2):
    print i

members = list(range(1, 10))
print members

i = 2
print i ** 2

squares = []

for i in range(1, 10):
    squares.append(i ** 2)

print squares

print min(squares)
print max(squares)

names = ["daniel", "hulei", "xx"]
# like golang slice
print names[0:2]

# copy from src
names_cp = names
names.append("....")

print names_cp
print names

dimensions = [2, 1]
print dimensions
print dimensions[1]

for i in dimensions:
    print i

try:
    dimensions[0] = 23

finally:
    print 1
