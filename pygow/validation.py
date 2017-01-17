import maybe

class Valid:
    a = None
    def __init__(self, a):
        self.a = a
    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.a == other.a)
    def __ne__(self, other):
        return not self.__eq__(other)
    def __str__(self):
        return 'Valid(%s)' % self.a
    def is_valid(self):
        return True
    def map(self, f):
        return Valid(f(self.a))
    def flat_map(self, f):
        return f(self.a)
    def ap(self, v):
        if v.is_valid():
            return Valid(self.a(v.a))
        else:
            return v
    def to_maybe(self):
        return maybe.Just(self.a)

class Invalid:
    es = None
    def __init__(self, es):
        self.es = es
    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.es == other.es)
    def __ne__(self, other):
        return not self.__eq__(other)
    def __str__(self):
        return 'Invalid(%s)' % self.es
    def is_valid(self):
        return False
    def map(self, f):
        return self
    def flat_map(self, f):
        return self
    def ap(self, v):
        if v.is_valid():
            return self
        else:
            return Invalid(self.es + v.es)
    def to_maybe(self):
        return maybe.Nothing()

def get_required_env(name):
    from os import getenv
    value = getenv(name)
    if value is None:
        return Invalid(['env var ' + name + ' required'])
    else:
        return Valid(value)

def lift_aN(arity, f):
    def curry(arity, f, acc = []):
        if arity == 1:
            def g(x):
                args = []
                args.extend(acc)
                args.append(x)
                return f(*args)
            return g
        else:
            def g(x):
                args = []
                args.extend(acc)
                args.append(x)
                return curry(arity - 1, f, args)
            return g
    if arity >= 1:
        return Valid(curry(arity, f))
    else:
        return Invalid(["n must be positive in lift_aN(n, f)"])

def lift_a(f):
    return lift_aN(1, f)

def lift_a2(f):
    return lift_aN(2, f)

def lift_a3(f):
    return lift_aN(3, f)
