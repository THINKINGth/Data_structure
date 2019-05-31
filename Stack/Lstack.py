# 顺序表实现堆栈
class Lstack:
    def __init__(self, init_len=8):
        self.top = 0
        self._elems = [0] * init_len
        self._len = init_len

    def is_empty(self):
        if self.top == 0:
            return True
        else:
            return False

    def push(self, num):
        if self.depth() == self._len:
            self._extend()

        self._elems[self.top] = num
        self.top += 1

    def pop(self):
        if self.is_empty():
            raise Exception
        else:
            self.top -= 1
            e = self._elems[self.top]
            return e

    def depth(self):
        return self.top

    def prints(self):
        p = self.top - 1
        while p >= 0:
            print(self._elems[p], end=' ')
            p -= 1

    def _extend(self):
        old_len = self._len
        new_len = self._len * 2
        self._len = new_len
        new_elems = [0] * new_len
        for i in range(old_len):
            new_elems[i] = self._elems[i]
        self._elems = new_elems


def _test():
    st = Lstack()
    st.push(5)
    st.push(4)
    st.push(3)
    st.push(2)
    st.push(1)
    st.push(0)
    st.prints()
    print()
    st.push(5)
    st.push(4)
    st.pop()
    st.prints()

_test()


