# coding=utf-8


pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)


def greet_user():
    print "hi baby"


print "begin"
greet_user()
