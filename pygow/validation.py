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

def get_required_env(name):
    from os import getenv
    value = getenv(name)
    if value is None:
        return Invalid(['env var ' + name + ' required'])
    else:
        return Valid(value)

def lift_a(f):
    return Valid(f)

def lift_a2(f):
    def f1(x1):
        def f2(x2):
            return f(x1, x2)
        return f2
    return Valid(f1)

def lift_a3(f):
    def f1(x1):
        def f2(x2):
            def f3(x3):
                return f(x1, x2, x3)
            return f3
        return f2
    return Valid(f1)

def lift_a4(f):
    def f1(x1):
        def f2(x2):
            def f3(x3):
                def f4(x4):
                    return f(x1, x2, x3, x4)
                return f4
            return f3
        return f2
    return Valid(f1)

def lift_a5(f):
    def f1(x1):
        def f2(x2):
            def f3(x3):
                def f4(x4):
                    def f5(x5):
                        return f(x1, x2, x3, x4, x5)
                    return f5
                return f4
            return f3
        return f2
    return Valid(f1)

def lift_a6(f):
    def f1(x1):
        def f2(x2):
            def f3(x3):
                def f4(x4):
                    def f5(x5):
                        def f6(x6):
                            return f(x1, x2, x3, x4, x5, x6)
                        return f6
                    return f5
                return f4
            return f3
        return f2
    return Valid(f1)

def lift_a7(f):
    def f1(x1):
        def f2(x2):
            def f3(x3):
                def f4(x4):
                    def f5(x5):
                        def f6(x6):
                            def f7(x7):
                                return f(x1, x2, x3, x4, x5, x6, x7)
                            return f7
                        return f6
                    return f5
                return f4
            return f3
        return f2
    return Valid(f1)

def lift_a8(f):
    def f1(x1):
        def f2(x2):
            def f3(x3):
                def f4(x4):
                    def f5(x5):
                        def f6(x6):
                            def f7(x7):
                                def f8(x8):
                                    return f(x1, x2, x3, x4, x5, x6, x7,
                                             x8)
                                return f8
                            return f7
                        return f6
                    return f5
                return f4
            return f3
        return f2
    return Valid(f1)

def lift_a9(f):
    def f1(x1):
        def f2(x2):
            def f3(x3):
                def f4(x4):
                    def f5(x5):
                        def f6(x6):
                            def f7(x7):
                                def f8(x8):
                                    def f9(x9):
                                        return f(x1, x2, x3, x4, x5, x6,
                                                 x7, x8, x9)
                                    return f9
                                return f8
                            return f7
                        return f6
                    return f5
                return f4
            return f3
        return f2
    return Valid(f1)
