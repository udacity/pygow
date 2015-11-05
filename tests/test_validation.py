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
def test_lift_a():
    def append(a):
        return a
    assert_equals(
        validation.Valid('a'),
        validation.lift_a(append).ap(a_v)
    )

b_v = validation.Valid('b')
def test_lift_a2():
    def append_2(a, b):
        return a + b
    assert_equals(
        validation.Valid('ab'),
        validation.lift_a2(append_2).ap(a_v).ap(b_v)
    )

c_v = validation.Valid('c')
def test_lift_a3():
    def append_3(a, b, c):
        return a + b + c
    assert_equals(
        validation.Valid('abc'),
        validation.lift_a3(append_3).ap(a_v).ap(b_v).ap(c_v)
    )

d_v = validation.Valid('d')
def test_lift_a4():
    def append_4(a, b, c, d):
        return a + b + c + d
    assert_equals(
        validation.Valid('abcd'),
        validation.lift_a4(append_4).ap(a_v).ap(b_v).ap(c_v).ap(d_v)
    )

e_v = validation.Valid('e')
def test_lift_a5():
    def append_5(a, b, c, d, e):
        return a + b + c + d + e
    assert_equals(
        validation.Valid('abcde'),
        validation.lift_a5(append_5).ap(a_v).ap(b_v).ap(c_v).ap(d_v).ap(e_v)
    )

f_v = validation.Valid('f')
def test_lift_a6():
    def append_6(a, b, c, d, e, f):
        return a + b + c + d + e + f
    assert_equals(
        validation.Valid('abcdef'),
        validation.lift_a6(append_6).ap(a_v).ap(b_v).ap(c_v).ap(d_v).ap(e_v).ap(f_v)
    )

g_v = validation.Valid('g')
def test_lift_a7():
    def append_7(a, b, c, d, e, f, g):
        return a + b + c + d + e + f + g
    assert_equals(
        validation.Valid('abcdefg'),
        validation.lift_a7(append_7).ap(a_v).ap(b_v).ap(c_v).ap(d_v).ap(e_v).ap(f_v).ap(g_v)
    )

h_v = validation.Valid('h')
def test_lift_a8():
    def append_8(a, b, c, d, e, f, g, h):
        return a + b + c + d + e + f + g + h
    assert_equals(
        validation.Valid('abcdefgh'),
        validation.lift_a8(append_8).ap(a_v).ap(b_v).ap(c_v).ap(d_v).ap(e_v).ap(f_v).ap(g_v).ap(h_v)
    )

i_v = validation.Valid('i')
def test_lift_a9():
    def append_9(a, b, c, d, e, f, g, h, i):
        return a + b + c + d + e + f + g + h + i
    assert_equals(
        validation.Valid('abcdefghi'),
        validation.lift_a9(append_9).ap(a_v).ap(b_v).ap(c_v).ap(d_v).ap(e_v).ap(f_v).ap(g_v).ap(h_v).ap(i_v)
    )
