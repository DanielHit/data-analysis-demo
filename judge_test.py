# coding:utf-8


print "hello world"

i = 1

if i == 1:
    print 1
#     elif
elif i == 3:
    print i
else:
    print i + 4

lists = []

if lists:
    print "empty"
else:
    print "not empty"

# test for loop to do the work

p = {"age": 2, "name": "dan iel"}
p1 = {"age": 2, "name": "dan iel"}
p2 = {"age": 2, "name": "dan iel"}

p_list = [p, p1, p2]

# 拟合
for body in p_list:
    for k in body.values():
        print k
