import poch

def test_binom():
    """Test binom with pytest."""
    # http://oeis.org/A000984
    oeis = [1,2,6,20,70,252,924,3432,12870,48620,184756,
    705432,2704156,10400600,40116600,155117520,
    601080390,2333606220,9075135300,35345263800,
    137846528820,538257874440,2104098963720,
    8233430727600,32247603683100,126410606437752,
    495918532948104,1946939425648112]
    result = list()
    for n in range(28):
        result += [poch.binom(2*n, n)]
    assert result == oeis


def test_stirling():
    """Test srirling with pytest."""
    # http://oeis.org/A008275
    oeis = [1,-1,1,2,-3,1,-6,11,-6,1,24,-50,35,-10,1,-120,
    274,-225,85,-15,1,720,-1764,1624,-735,175,-21,1,
    -5040,13068,-13132,6769,-1960,322,-28,1,40320,
    -109584,118124,-67284,22449,-4536,546,-36,1,
    -362880,1026576,-1172700,723680,-269325,63273,
    -9450,870,-45,1]
    result = list()
    for n in range(1, 11):
        for k in range(1, n + 1):
            result += [poch.stirling(n, k)]
    assert result == oeis


def test_factorial():
    """Test recursive factorial with pytest."""
    assert poch.factorial(0) == 1
    assert poch.factorial(1) == 1
    assert poch.factorial(2) == 2
    assert poch.factorial(3) == 6
    assert poch.factorial(4) == 24
    assert poch.factorial(5) == 120
    assert poch.factorial(6) == 720
    assert poch.factorial(7) == 5040
    assert poch.factorial(8) == 40320
    assert poch.factorial(9) == 362880
    assert poch.factorial(10) == 3628800


def test_poch():
    """Test poch with pytest.
    First test data and inline comments by stdlib-js @github, the standard library
    for JavaScript and Node.js.
    Second test data by RussellAndrewEdson @github
    """
    # First.
    assert poch.poch(0.9, 5) == 94.76649000000002
    assert poch.poch(-9, 3) == -504
    assert poch.poch(3, -2) == 0.5
    # The function returns '1' if provided 'n = 0' and a nonnegative 'x'.
    assert poch.poch(2, 0) == 1
    assert poch.poch(0.2, 0) == 1
    assert poch.poch(-2, 0) == 1
    assert poch.poch(-0.2, 0) == 1
    # The function returns '0' if provided 'x = 0' and a positive 'n'.
    assert poch.poch(0, 4) == 0
    assert poch.poch(0, 1) == 0
    # The function returns -n! if provided 'x = 0' and a negative 'n'.
    assert poch.poch(0, -1) == -1
    # Second.
    assert poch.poch(3, 4) == 360
    assert poch.poch(17, 17) == 415017197290314178560000
    assert poch.poch(-3, -4) == 0.0011904761904761906
