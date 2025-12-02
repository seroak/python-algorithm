# 1.격자의 왼쪽 위는 1,1 오른쪽 아래는 4,4
# 2.모든 물고기는 한칸 이동하는데 상어가 있는 칸, 물고기의 냄새가 있는 칸,
# 격자의 범위를 벗어나는 칸으로는 이동 할 수 없다
# 각 물고기는 자신이 가지고 있는 이동 방향이 이동할 수 있는 칸을 향할 때까지
# 방향을 45도 반시계 회전시킨다 만앾 끝까지 이동할 수 없다면 이동하지 않는다
# 상어는 연속해서 3칸 이동한다
# 이동중에 격자 범위를 벗어나느 칸이 있으면 그 방법은 불가능한 이동 방법이다
# 상어가 물고기가 있는 칸으로 이동하게 된다면 그 칸에 있는 모든 물고기는 격자에서 제외되며
# 제외되는 모든 물고기는 물고기 냄새를 남긴다
# 가능한 이동 방법 중에서 제외되는 물고기의 수가 가장 많은 방법으로 이동하며
# 그러한 방법이 여러가지인 경우 사전 순으로 가장 앞서는 방법을 이용한다
# 냄새는 사이클이 지나면 냄새는 사라진다
# 1에서 사용한 복제 마법이 완료되고 모든 복제된 물고기는 1에서의 위치와 방향을 그대로 갖는다
from tkinter import *
from random import *


class Store:
    def __init__(self):
        self.i = None
        self.j = None

    def post(self, i, j):
        self.i = i
        self.j = j

    def get(self):
        return self.i, self.j


store = Store()


def process1():
    i = randint(0, 100)
    j = randint(0, 100)
    store.post(i, j)
    e1.insert(0, ('%d*%d' % (i, j)))


def process2():
    i, j = store.get()
    a = i * j
    if (a == int(e2.get())):
        e3.insert(0, '맞았습니다.')
    else:
        e3.insert(0, '틀렸습니다.')


window = Tk()

l1 = Label(window, text='문제')
l2 = Label(window, text='답 입력')
l3 = Label(window, text='정답 체크')
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)
l3.grid(row=2, column=0)

e1 = Entry(window, bg='yellow')
e2 = Entry(window, bg='yellow')
e3 = Entry(window, bg='yellow')
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

b1 = Button(window, text="새 문제", command=process1)
b1.grid(row=3, column=0)
b2 = Button(window, text="답 보기", command=process2)
b2.grid(row=3, column=1)

window.mainloop()
