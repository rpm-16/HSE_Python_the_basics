from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, arg, other):
        self.matrix1 = arg
        self.matrix2 = other


class Matrix:
    def __init__(self, arg):
        self.list = deepcopy(arg)

    def size(self):
        return (len(self.list), len(self.list[0]))

    def __str__(self):
        string = ''
        for line in self.list:
            string += '\t'.join(map(str, line)) + '\n'
        return string.rstrip()

    def __add__(self, other):
        if len(self.list) != len(other.list):
            error = MatrixError(self, other)
            raise error
        else:
            sumList = []
            for i in range(len(self.list)):
                sumList.append(
                    list(a + b for a, b in zip(self.list[i], other.list[i]))
                    )
            return Matrix(sumList)

    def __mul__(self, alpha):
        endList = []
        string = ''
        for i in range(len(self.list)):
            endList.append(list(a * alpha for a in self.list[i]))
        for line in endList:
            string += '\t'.join(map(str, line)) + '\n'
        return string.rstrip()

    __rmul__ = __mul__

    def transpose(self):
        string = ''
        self.list = [list(i) for i in zip(*self.list)]
        return Matrix(self.list)

    @staticmethod
    def transposed(m):
        string = ''
        m1 = [list(i) for i in zip(*m.list)]
        return Matrix(m1)

exec(stdin.read())
