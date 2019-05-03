# 单链表
class Node:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next_ = next_

class LList:
    def __init__(self):
        self.head = None

    # 链表前端加入元素
    def prepend(self, elem):
        self.head = Node(elem, self.head)

    # 链表尾端加入元素
    def append(self, elem):
        if self.head is None:
            self.head = Node(elem)
        else:
            p = self.head
            while p.next_ is not None:
                p = p.next_
            p.next_ = Node(elem)

    # 尾端删除并返回链表的元素
    def pop(self):
        if self.head is None:
            return "错误, 链表为空"
        else:
            p = self.head
            while p.next_.next_ is not None:
                p = p.next_
            i = p.next_
            p.next_ = None
            return i

    # 前端删除并返回链表的元素
    def pop_first(self):
        if self.head is None:
            return "错误，链表为空"
        else:
            p = self.head
            self.head = self.head.head
            return p

    # 遍历打印链表的元素
    def prints(self):
        p = self.head
        while p.next_ is not None:
            print(p.elem, end=' ')
            p = p.next_
        print(p.elem)

    # 返回链表的长度
    def length(self):
        p = self.head
        lens = 0
        while p is not None:
            p = p.next_
            lens += 1
        return lens

    # 判断链表是否为空
    def empty(self):
        if self.head is None:
            return True

    # 任意位置插入元素
    def insert(self, loc, elem):
        if self.length() < loc:
            return '插入位置错误'
        p = self.head
        if loc == 0:
            self.prepend(elem)
            return
        for i in range(loc - 1):
            p = p.next_
        p.next_ = Node(elem, p.next_)

    # 单链表的插入排序
    def sorting(self):
        if self.head is not None:
            p = self.head
            crt = p.next_
            while crt is not None:
                p = self.head
                y = crt.elem
                while p is not crt and p.elem < crt.elem:
                    p = p.next_
                while p is not crt:
                    x = p.elem
                    p.elem = y
                    y = x
                    p = p.next_
                crt.elem = y
                crt = crt.next_

    # 单链表的插入排序
    def sort(self):
        p = self.head
        if p and p.next_ is None:
            return
        rem = p.next_
        p.next_ = None
        while rem is not None:
            p = self.head
            q = None
            while p is not None and p.elem < rem.elem:
                q = p
                p = p.next_
            if q is None:
                self.head = rem
            else:
                q.next_ = rem
            q = rem
            rem = rem.next_
            q.next_ = p




