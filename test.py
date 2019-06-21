print 1


def hello():
    print "what a pitty"
    return


def name():
    return "daniel hello"


hello()
print name()

age = "daniel hi   "

print age.strip()
print len(age)
print len(age.strip())

print (" we".strip())

age = 23

name = "23"


students = ["jack", "rose", 23]
print students

for s in students:
    print str(s) + "hello"

print students[0]
print students[-1]
print students[0].title()
print students[0].capitalize()

del students[-1]
print students

students.append("fuck me")
print students

print students.pop()

students.reverse()
print students



