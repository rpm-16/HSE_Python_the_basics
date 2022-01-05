from sys import stdin
import copy


class Matrix:

    def __init__(self, listsum):
        self.list = copy.deepcopy(listsum)

    def __str__(self):
        string = ''
        for line in self.list:
            string += '\t'.join(map(str, line)) + '\n'
        return string.rstrip()

    def size(self):
        return (len(self.list), len(self.list[0]))

exec(stdin.read())
