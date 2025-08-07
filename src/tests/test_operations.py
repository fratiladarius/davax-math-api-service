from math_operations.power_op import PowerOperation
from math_operations.fibonacci_op import FibonacciOperation
from math_operations.factorial_op import FactorialOperation
import pytest


def test_power_op():
    op = PowerOperation()
    assert op.execute(2, 5) == 32
    assert op.execute(0, 5) == 0
    assert op.execute(2, 0) == 1
    assert op.execute(1, 1000) == 1


def test_fibonacci_op():
    op = FibonacciOperation()
    assert op.execute(0) == 0
    assert op.execute(1) == 1
    assert op.execute(2) == 1
    assert op.execute(10) == 55


def test_factorial_op():
    op = FactorialOperation()
    assert op.execute(0) == 1
    assert op.execute(1) == 1
    assert op.execute(4) == 24
    assert op.execute(6) == 720


def test_fibonacci_negative():
    op = FibonacciOperation()
    with pytest.raises(ValueError):
        op.execute(-1)


def test_factorial_negative():
    op = FactorialOperation()
    with pytest.raises(ValueError):
        op.execute(-5)
