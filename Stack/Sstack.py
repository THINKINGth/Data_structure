# 单链表实现堆栈
class Node:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next_ = next_


class Sstack:
    def __init__(self):
        self.top = None

    def push(self, num):
        self.top = Node(num, self.top)

    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False

    def pop(self):
        if self.is_empty():
            raise Exception
        e = self.top
        self.top = self.top.next_
        return e.elem

    def depth(self):
        p = self.top
        length = 0
        while p is not None:
            len += 1
            p = p.next_
        return length

    def prints(self):
        p = self.top
        while p is not None:
            print(p.elem, end=' ')
            p = p.next_






