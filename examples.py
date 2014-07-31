#!/usr/bin/env python


class MyClass(object):
    """docstring"""
    some_var = True
    another = 0

    def f(self):
        return self.another

    # for x in range(10):  # unusual, valid
    #     another += x


c = MyClass()
#print c.another
print MyClass.__mro__