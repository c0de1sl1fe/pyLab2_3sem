from task1 import Iterator1_img, iterator1, run_1
from task2 import run_2
from task3 import run_3
from task4 import run_4
from task5 import run_5

if __name__ == '__main__':
    a = Iterator1_img('test', "D:\Git\pyLab2_3sem\dataset")
    print(a.__next__())
    print(a.__next__())
    print(a.__next__())
    print(a.clear())
    print(a.__next__())
    print(a.__next__())
    print(a.__next__())