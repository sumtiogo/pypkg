import inspect


def add(a, b, f):
    """A add function.

    Args:
      a (float): a
      b (float): b
      f (float -> float): a mapping function

    Returns:
      float: f(a) + f(b)

    Examples:
      >>> import yamath
      >>> yamath.add(1.0, 2.0, lambda x: 2*x)
      6.0
      >>> yamath.add(1.0, 2.0, None)
      Traceback (most recent call last):
        ...
      TypeError: f should be a function, you idiot!

    Raises:
      TypeError: if f is not a fucntion

    """

    if not inspect.isfunction(f):
        raise TypeError('f should be a function, you idiot!')

    return f(a) + f(b)
