def foo_new(cls):
    print("about to construct an instance of", cls)
    obj = object.__new__(cls)
    print(obj, 'is a new instance of', cls)
    return obj


def foo_init(self):
    print("initializing", self)


Foo = type('Foo', (object,), {'__new__': foo_new, '__init__': foo_init})

Foo()
