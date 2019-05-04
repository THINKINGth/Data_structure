# 顺序表实现队列
class Squeue:
    def __init__(self, init_len=8):
        self._len = init_len
        self._head = 0
        self._num = 0
        self._elems = [0] * init_len

    def is_empty(self):
        if self._num == 0:
            return True
        else:
            return False

    def peek(self):
        if self.is_empty():
            raise Exception
        else:
            return self._elems[self._head]

    def enqueue(self, num):
        if self._num == self._len:
            self.extends()
        self._elems[(self._head + self._num) % self._len] = num
        self._num += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception
        else:
            e = self._elems[self._head]
            self._head = (self._head + 1) % self._len
            self._num -= 1
            return e

    def extends(self):
        old_len = self._len
        new_len = self._len * 2
        new_elems = [0] * new_len
        self._len = new_len
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head + i) % old_len]
        self._elems = new_elems
        self._head = 0

    def prints(self):
        for i in range(self._num):
            print(self._elems[(self._head + i) % self._len], end=' ')
        print()
