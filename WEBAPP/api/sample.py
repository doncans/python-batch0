# a = 10

# def fun(a):
#     return a
# l1 = [2,3,4,5]
# def fun(l1=[]):
#     l1.append(10)
#     return l1



# t = (3,4,6,3,2,1)

# sorted(t, key=1)

# import re

# txt = "india got independence on 1947 aug 15 and Gandhiji played a key role"

# # re.findall('\d+\s+d+', txt)
# re.findall(r'[0-9]{4}\+\S\[0-9]{2}', txt)
import collections
d = {"name":"ramesh","age":32,"sex":"male"}

od = collections.OrderedDict(sorted(d.items()))
print(dict(od))


