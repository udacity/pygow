from nose.tools import assert_true, assert_false, assert_equals
from pygow import maybe, validation

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

def test_eq():
  assert_true(maybe.Just(42).__eq__(maybe.Just(42)))
  assert_false(maybe.Just(42).__eq__(maybe.Just(1)))
  assert_true(maybe.Nothing().__eq__(maybe.Nothing()))
  assert_false(maybe.Just(42).__eq__(maybe.Nothing()))

def test_ne():
  assert_false(maybe.Just(42).__ne__(maybe.Just(42)))
  assert_true(maybe.Just(42).__ne__(maybe.Just(1)))
  assert_false(maybe.Nothing().__ne__(maybe.Nothing()))
  assert_true(maybe.Just(42).__ne__(maybe.Nothing()))

def test_str():
  assert_equals('Just(42)', str(maybe.Just(42)))
  assert_equals('Nothing()', str(maybe.Nothing()))

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

def test_parse_int():
  assert_equals(maybe.Just(42), maybe.parse_int('42'))
  assert_equals(maybe.Nothing(), maybe.parse_int('forty-two'))

def test_maybe():
  assert_true(maybe.maybe(None).__eq__(maybe.Nothing()))
  assert_true(maybe.maybe(42).__eq__(maybe.Just(42)))

def test_or_else():
  assert_true(maybe.Just(42).__eq__(maybe.Just(42).or_else(maybe.Just(1))))
  assert_true(maybe.Just(1).__eq__(maybe.Nothing().or_else(maybe.Just(1))))

def test_to_validation():
  assert_equals(validation.Valid(42), maybe.Just(42).to_validation('nope'))
  assert_equals(validation.Invalid(['nope']), maybe.Nothing().to_validation('nope'))
