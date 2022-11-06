from task1 import run_1, iterator1, Iterator1_img
from task2 import run_2
from task3 import run_3
from task4 import run_4
from task5 import run_5



if __name__ == '__main__':
    a = Iterator1_img('test')
    print(a.__next__())
    print(a.__next__())
    print(a.__next__())
    print(a.clear())
    print(a.__next__())
    print(a.__next__())
    print(a.__next__())