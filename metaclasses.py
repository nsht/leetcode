class Foo:
    def __new__(cls):
        print("about to construct an instance of",cls)
        obj = super().__new__(cls)
        print(obj,'is a new instance of',cls)
        return obj
    def __init__(self):
        print("initializing",self)

Foo()
"""
Source https://twitter.com/1st1/status/1160956397216866305
Prints
about to construct an instance of <class '__main__.Foo'>
<super: <class 'Foo'>, <Foo object>>
<__main__.Foo object at 0x7f6d9c06acc0> is a new instance of <class '__main__.Foo'>
init <__main__.Foo object at 0x7f6d9c06acc0>
"""
