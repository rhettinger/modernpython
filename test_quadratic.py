from hypothesis import given, assume, strategies as st
from quadratic import quadratic
import cmath

@given(a = st.floats(min_value=-10000, max_value=10000),
       b = st.floats(min_value=-10000, max_value=10000),
       c = st.floats(min_value=-10000, max_value=10000))
def test_quad(a, b, c):
    assume(abs(a) >= 0.0001)
    x1, x2 = quadratic(a, b, c)
    assert cmath.isclose(a*x1**2 + b*x1 + c, 0.0, abs_tol=0.0001)
    assert cmath.isclose(a*x1**2 + b*x1 + c, 0.0, abs_tol=0.0001)


if __name__ == '__main__':

    test_quad()
