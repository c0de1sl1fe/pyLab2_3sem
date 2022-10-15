from task1 import run_1, iterator1
from task2 import run_2
from task3 import run_3
from task4 import run_4
from task5 import run_5

def numbers_range(n):
    for i in range(n):
        yield i
    return None

if __name__ == '__main__':
    print("Begin of lab!")
    # run_1("test")
    # run_2('D:/for_test/' , "test")
    # run_2('D:/for_test/' , "z_ttest")
    # run_3('test',"D:/for_test/")
    it = numbers_range(5)
    for i in it:
        print(i)
    # print(next(tmp))
    # print(tmp)
    # print(tmp)
    # print(tmp)