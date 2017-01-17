import validation

class Just:
    a = None
    def __init__(self, a):
        self.a = a
    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.a == other.a)
    def __ne__(self, other):
        return not self.__eq__(other)
    def __str__(self):
        return 'Just(%s)' % self.a
    def is_just(self):
        return True
    def map(self, f):
        return Just(f(self.a))
    def flat_map(self, f):
        return f(self.a)
    def get_or_else(self, x):
        return self.a
    def or_else(self, x):
        return self
    def to_validation(self, e):
        return validation.Valid(self.a)

class Nothing:
    def __eq__(self, other):
        return isinstance(other, self.__class__)
    def __ne__(self, other):
        return not self.__eq__(other)
    def is_just(self):
        return False
    def __str__(self):
        return 'Nothing()'
    def map(self, f):
        return Nothing()
    def flat_map(self, f):
        return Nothing()
    def get_or_else(self, x):
        return x
    def or_else(self, x):
        return x
    def to_validation(self, e):
        return validation.Invalid([e])

def get_maybe_env(name):
    from os import getenv
    value = getenv(name)
    if value is None:
        return Nothing()
    else:
        return Just(value)

def non_empty_string(x):
    if len(x.strip()) is 0:
        return Nothing()
    else:
        return Just(x)

def parse_int(x):
    try:
        return Just(int(x))
    except:
        return Nothing()

def maybe(x):
    if x is None:
        return Nothing()
    else:
        return Just(x)
