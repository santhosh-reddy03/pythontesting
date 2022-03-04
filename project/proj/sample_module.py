import re, warnings

def add(a, b):
    return a+b


class SampleClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self: any, p: int) -> int:
        return self.a + self.b + p

    def mul(self) -> int:
        return self.a * self.b

    def divide(self) -> float or int:
        return self.a / self.b


# def f1(data):
#     p = re.compile('(?P[A-Z]{2,3}) (?P[0-9]{3})')
#     return p.search(data)

# obj = f1('CS 101')
# # print(obj.group('x'), obj.group('y'))
# print(obj['x'], obj['y'])
# print(obj[0], obj[1])
def depreacated(func):
    def wrapper(*args, **kwargs):
        warnings.warn("deprecated function {}".format(func.__name__), category=DeprecationWarning)
        return func(*args, **kwargs)
    return wrapper

@depreacated
def prod(x,y):
    'returns product of two numbers'
    return x*y

print(prod(12,12))
print(prod.__name__)
print(prod.__doc__)

class MyTupe(type):
    pass

class SubT(MyTupe):
    pass

class MyOb(object):
    __metaclass__ = MyTupe
    pass

print(MyTupe.__class__)
print(SubT.__class__)
print(MyOb.__class__)

print('{0:$>2d}*{1:$>2d}={2:$>2d}'.format(2,3,2*3))

def f1(a,b):
    f1.s = 'some value'
    return a + b

try:
    print(f1.s)
except Exception as e:
    print(str(e))

f1(3,4)

try:
    print(f1.s)
except Exception as e:
    print(str(e))

class grandpa(object):
    pass

class father(grandpa):
    pass

class mother(object):
    pass

class child(mother, father):
    pass

print(child.__mro__)

class A: pass

class B: pass
B.__metaclass__=A




class C(object): pass

class D(C): pass
print(B)
# a = A()
# b = B()
# c = C()
# d = D()

# print(isinstance(a, type(B)))
# print(issubclass(C, C))
# print(isinstance(d, D))
# print(issubclass(C, (D, A, B, C)))


def foo(n):
    if (n<3): 
        yield 1
    else:
        return 
    yield 2
n = 2

# f = foo(n)
# for i in range(n):
#     print(next(f))

# n = 5
# f = foo(n)
# for i in range(n):
#     print(next(f))

    
t = tuple(1, 2,3)
print(t)

