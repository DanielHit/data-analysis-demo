from collections import OrderedDict
from random import randint

# test different order diction
favorite_languages = OrderedDict()

favorite_languages["jen"] = "python"

for k, v in favorite_languages.items():
    print k.title(), v

x = 10
while x > 5:
    x = randint(1, 100)
    print x

print x
