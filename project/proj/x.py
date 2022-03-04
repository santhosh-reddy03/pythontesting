import sys, builtins
import logging

# sys.builtins.__dict__.keys()
sys.builtin_module_names
# sys.module_names

logging.warning("A warning")
logging.info("A info")
logging.error("An error")
logging.debug("debug")

class Person(object):
    def __init__(self, name):
        # self.name = name
        print("Hello my name is " + name)

class Bob(Person):
    def __init__(self, name='Bob'):
        print("name is bob")
    def classId(self):
        print("i m father")

class Sue(Person):
    def __init__(self, name='Sue'):
        print("name is sue")
    def classId(self):
        print("i m mother")
    
class Child(Bob, Sue):
    def __init__(self, name='x'):
        super(Child, self).__init__(name)
    def classId(self):
        print("i m child")

Ann = Child("aann")
Ann.classId()
a = (5)
print(type(a))

try:
    print("gell")
    raise ValueError("some")
except ValueError as e:
    print(e)

a = 1

def f1():
    x = 1,2,3
    y = a
f1()

def smart_d(fu):
    def wrapper(*args):
        a, b = args
        if b==0:
            print("cant divide")
            return
        return fu(a,b)
    return wrapper

@smart_d
def div(a,b):
    return a/b
print(div.__name__)
print(4/16)
print(div(2,0))


class B(object):
    def __init__(self) -> None:
        print("base")

class C(B):
    def __init__(self) -> None:
        super(C).__init__()
        print("child")
b = B()
c = C()

a = [1,2]
d = [3,4]
print(dict(zip(a,d)))
