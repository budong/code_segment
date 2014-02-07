#!/usr/bin/env python2.7
class Row(dict):
    """A dict that allows for object-like property access syntax."""
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

D={'a':1,'b':2,'c':3,'d':4} 

dict_instance=Row(D)
print dict_instance.a
