from typing import TypeVar

Numeric = TypeVar('Numeric', int, float, complex)
EMPTY_SUM = 0
MINUS_ONE = -1

_stirling1_computed = dict()

def stirling(n: int, k: int) -> int:
    """Pure Python signed Stirling numbers of the first kind, n cycle k.
    Published by Stirling in 1730.
    To calculate unsigned Stirling numbers of the first kind, call abs(stirling(n, k)).
    """
    key = (n, k)

    if key in _stirling1_computed.keys():
        return _stirling1_computed[key]
    if not n and not k:
        return 1
    elif n < 0 or k < 0 or k > n:
        return 0
    _stirling1_computed[key] = stirling(dec(n), dec(k)) - (dec(n))*stirling(dec(n), k)
    return _stirling1_computed[key]


def poch(z: Numeric, n: int) -> Numeric:
    """Pure Python Pochhammer symbol (z)_n using Stirling numbers of the first kind.
    Recursive when n is negative. Also called rising factorial.
    """
    # (z)_-n=1/(z-n)_n.
    if n < 0:
        return 1/poch(z + n, -n)  # N.B. flipped signs on n.
    sum = EMPTY_SUM
    # (z)_n=sum_k=0^n (-1)^k+n s(n,k)z^k.
    for k in range(inc(n)):
        sum += MINUS_ONE**(k + n)*stirling(n, k)*z**k
    return sum


def factorial(integer: int) -> int:
    """Pure Python recursive factorial function."""
    if integer < 2:
        return 1
    return integer*factorial(dec(integer))

inc = lambda x: x + 1
dec = lambda x: x - 1
pochhammer_symbol = poch
binom = lambda n, k: poch(inc(k), n - k)//factorial(n - k)
binomial_coefficient = binom
