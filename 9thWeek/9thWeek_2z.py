from sys import stdin
import copy


class Matrix:

    def __init__(self, listA):
        self.list = copy.deepcopy(listA)

    def __str__(self):
        string = ''
        for line in self.list:
            string += '\t'.join(map(str, line)) + '\n'
        return string.rstrip()

    def __add__(self, other):
        sumList = []
        for i in range(len(self.list)):
            string = ''
            sumList.append(
                list(a + b for a, b in zip(self.list[i], other.list[i]))
                )
            for line in sumList:
                string += '\t'.join(map(str, line)) + '\n'
        return string.rstrip()

    def __mul__(self, alpha):
        endList = []
        string = ''
        for i in range(len(self.list)):
            endList.append(list(a * alpha for a in self.list[i]))
        for line in endList:
            string += '\t'.join(map(str, line)) + '\n'
        return string.rstrip()

    __rmul__ = __mul__

    def size(self):
        return (len(self.list), len(self.list[0]))

exec(stdin.read())
