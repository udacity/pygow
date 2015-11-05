from nose.tools import assert_true, assert_false, assert_equals
from pygow import maybe

def multBy(x):
    def k(y):
        return x * y
    return k

def divBy(x):
    def k(y):
        if (x == 0):
            return maybe.Nothing()
        else:
            return maybe.Just(y / x)
    return k

def test_is_just():
  assert_true(maybe.Just(42).is_just())
  assert_false(maybe.Nothing().is_just())

def test_map():
  assert_equals(maybe.Just(42), maybe.Just(6).map(multBy(7)))
  assert_equals(maybe.Nothing(), maybe.Nothing().map(multBy(7)))

def test_flat_map():
  assert_equals(maybe.Just(6), maybe.Just(42).flat_map(divBy(7)))
  assert_equals(maybe.Nothing(), maybe.Nothing().flat_map(divBy(7)))

def test_get_or_else():
  assert_equals(42, maybe.Just(42).get_or_else(1))
  assert_equals(1, maybe.Nothing().get_or_else(1))

def test_get_maybe_env():
  assert_true(maybe.get_maybe_env('HOME').is_just())
  assert_false(maybe.get_maybe_env('THIS_AINT_AN_ENV_VAR').is_just())

def test_non_empty_string():
  assert_true(maybe.non_empty_string('foo').is_just())
  assert_false(maybe.non_empty_string('   ').is_just())
