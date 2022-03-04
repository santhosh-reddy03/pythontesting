i = 5
print(i.__add__(4))
print('ab12'.isalnum())
print("some".isidentifier())
print("Ab!2".swapcase())

def f(i, values=[]):
    values.append(i)
    return values

f(1)
f(2)
v = f(3)
print(v)
print(1 in v)
print(1 in set(v))

print([i for i in v if i > 1])
v.append([1,3])
print(v)

names1 = ['Amir', 'Bob', 'Cindy', 'Diana']
names2 = [name.lower() for name in names1]
print(names2[2][0])
t,c,b = 1,3,2
print(t,c,b)

print(len(set([1,1,2,3,4,4,3,3])))
print({a**2 for a in range(4)})

d = {'a':1, 'b':2}

del d['a']
print(d)

m = {}
m[2] = 1
m[1] = [2,3,4]
print(m[1][1])
print(m)
print(-18//4)
print(10-4*2)

class Change:
    def __init__(self, x, y, z) -> None:
        self.a = x+y+z
    
    @staticmethod
    def ax(x):
        print(x)



X = Change(1,2,3)
y = getattr(X, 'a')
setattr(X, 'a', y+1)
print(X.a)
X.ax(1)
z = lambda x: x*y
print(z(2))
print(id(z))

print("  ab  a".lstrip())