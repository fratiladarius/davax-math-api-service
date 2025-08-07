from .operation_base import OperationBase


class FibonacciOperation(OperationBase):
    def execute(self, n):
        if n < 0:
            raise ValueError('n must be >= 0')
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
