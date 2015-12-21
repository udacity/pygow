from nose.tools import assert_true, assert_false, assert_equals
from pygow import validation

def multBy(x):
    def k(y):
        return x * y
    return k

def divBy(x):
    def k(y):
        if (x == 0):
            return validation.Invalid(['doh'])
        else:
            return validation.Valid(y / x)
    return k

def test_eq():
    assert_true(validation.Valid(42).__eq__(validation.Valid(42)))
    assert_false(validation.Valid(42).__eq__(validation.Valid(1)))
    assert_true(validation.Invalid(['doh']).__eq__(validation.Invalid(['doh'])))
    assert_false(validation.Valid(42).__eq__(validation.Invalid(['doh'])))

def test_ne():
    assert_false(validation.Valid(42).__ne__(validation.Valid(42)))
    assert_true(validation.Valid(42).__ne__(validation.Valid(1)))
    assert_false(validation.Invalid(['doh']).__ne__(validation.Invalid(['doh'])))
    assert_true(validation.Valid(42).__ne__(validation.Invalid(['doh'])))

def test_str():
    assert_equals('Valid(42)', str(validation.Valid(42)))
    assert_equals('Invalid([\'doh\'])', str(validation.Invalid(['doh'])))

def test_is_valid():
    assert_true(validation.Valid(42).is_valid())
    assert_false(validation.Invalid(['doh']).is_valid())

def test_map():
    assert_equals(validation.Valid(42), validation.Valid(6).map(multBy(7)))
    assert_equals(validation.Invalid(['doh']), validation.Invalid(['doh']).map(multBy(7)))

def test_flat_map():
    assert_equals(validation.Valid(6), validation.Valid(42).flat_map(divBy(7)))
    assert_equals(validation.Invalid(['doh']), validation.Invalid(['doh']).flat_map(divBy(7)))

def test_get_required_env():
    assert_true(validation.get_required_env('HOME').is_valid())
    assert_false(validation.get_required_env('THIS_AINT_AN_ENV_VAR').is_valid())

a_v = validation.Valid('a')
a_i = validation.Invalid(['invalid: a'])
def test_lift_a():
    def append(a):
        return a
    assert_equals(
        validation.Valid('a'),
        validation.lift_a(append).ap(a_v)
    )

b_v = validation.Valid('b')
b_i = validation.Invalid(['invalid: b'])
def test_lift_a2():
    def append_2(a, b):
        return a + b
    assert_equals(
        validation.Valid('ab'),
        validation.lift_a2(append_2).ap(a_v).ap(b_v)
    )
    assert_equals(
        validation.Invalid(['invalid: a']),
        validation.lift_a2(append_2).ap(a_i).ap(b_v)
    )
    assert_equals(
        validation.Invalid(['invalid: b']),
        validation.lift_a2(append_2).ap(a_v).ap(b_i)
    )
    assert_equals(
        validation.Invalid(['invalid: a', 'invalid: b']),
        validation.lift_a2(append_2).ap(a_i).ap(b_i)
    )

c_v = validation.Valid('c')
def test_lift_a3():
    def append_3(a, b, c):
        return a + b + c
    assert_equals(
        validation.Valid('abc'),
        validation.lift_a3(append_3).ap(a_v).ap(b_v).ap(c_v)
    )

def test_lift_a4():
    def append_4(a, b, c, d):
        return a + b + c + d
    assert_equals(
        validation.Valid('abca'),
        validation.lift_aN(4, append_4).ap(a_v).ap(b_v).ap(c_v).
                                        ap(a_v)
    )

def test_lift_a9():
    def append_9(a, b, c, d, e, f, g, h, i):
        return a + b + c + d + e + f + g + h + i
    assert_equals(
        validation.Valid('abcabcabc'),
        validation.lift_aN(9, append_9).ap(a_v).ap(b_v).ap(c_v).
                                        ap(a_v).ap(b_v).ap(c_v).
                                        ap(a_v).ap(b_v).ap(c_v)
    )

def test_lift_a0():
    def append(a):
        return a
    assert_equals(
        validation.Invalid(["n must be positive in lift_aN(n, f)"]),
        validation.lift_aN(0, append).ap(a_v)
    )
