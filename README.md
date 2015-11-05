Functional data structures for Python.

## Usage

```
$ pip install git+git://github.com/udacity/pygow.git@0.1
```

## Features

**Maybe**

A `Maybe` represents an optional value.  It can be either `Nothing`, or
`Just(a)` for some value `a`.

A `Maybe` instance includes the following methods:

* `is_just()`: Returns true if this is a `Just`, or false if it is a
  `Nothing`
* `map(f)`: Applies the function `f` to the underlying value `a`, if
  any, and returns a new `Maybe` containing it
* `flat_map(f)`: Applies the function `f` to the underlying value `a`, if
  any, and returns the resulting `Maybe` instance
* `get_or_else(x)`: Returns the underlying value `a`, if any, otherwise
  returns the parameter `x`

The `maybe` module includes the following functions:

* `get_maybe_env(name)`: Returns a `Maybe` of the named environment
  variable
* `non_empty_string(x)`: Returns a `Just` of the string `x` if it is
  non-empty, or `Nothing` otherwise

**Validation**

A `Validation` represents the result of a validation operation.  It can
be either `Valid(a)` for some value `a`, or `Invalid(es)` for some list
of errors `es`.

A `Valiation` instance includes the folling methods:

* `is_valid()`: Returns true if this is a `Valid`, or false if it is an
  `Invalid`
* `map(f)`: Applies the function `f` to the underlying value `a`, if
  any, and returns a new `Validation` containing it
* `flat_map(f)`: Applies the funciton `f` to the underlying value `a`,
  if any, and returns the resulting `Validation`
* `ap(v)`: Applies the underlying value `a`, which must be a function,
  to the value `v`, and returns the resulting `Validation`

The `validation` module includes the following functions:

* `get_required_env(name)`: Returns a `Validation` of the named
  environment variable
* `lift_a(f)`: Returns a `Valid` of the unary function `f`
* `lift_aN(f)`: Returns a `Valid` of a curried representation of the
  N-arity function `f`.  Defined for `N` from `2` to `9`.
