import os
import random

import shutil


def create_dir_copy_randNames(class_name: str, dst: str) -> None:
    '''Create array with rand num in 0 to 10000 length of names in source dir 
    and copy with that names to dst dir;
    and create descriprion .csv file like in task 1'''

    path = os.path.join("dataset", class_name)
    names = os.listdir(path)
    for j in names:
        if not ".jpg" in j:
            names.remove(j)
    tmp = random.sample(range(1, 10001), len(names))
    for i in range(len(names)):
        s = os.path.join(os.path.join('dataset', class_name), names[i])
        d = os.path.join(dst, f'{tmp[i]}.jpg')
        shutil.copy2(s, d)

    names = os.listdir(dst)
    with open(os.path.join(dst, "annotation.csv"), 'w') as file_csv:
        for i in names:
            if not ".jpg" in i:
                names.remove(i)
        for i in names:
            # writer.writerow(str(os.path.abspath(i) + "," + os.path.join(path, i) + "," + path_dir))
            file_csv.write(os.path.abspath(i) + "," +
                           os.path.join(dst, i) + "," + class_name)
            file_csv.write("\n")
    file_csv.close


def create_dir(path: str) -> str:
    '''this function create 'dataset' directory
     in path gived by user
     and return path of new_dataset dir'''
    if not os.path.isdir(os.path.join(path, 'dataset')):
        os.mkdir(os.path.join(path, 'dataset'))
    return os.path.join(path, 'dataset')


def iterator3(path: str) -> str:
    '''Just interater for direcrory'''
    names = os.listdir(path)
    for i in names:
        if not ".jpg" in i:
            names.remove(i)
    for i in range(len(names)):
        yield (names[i])
    return None


class Iterator3_img:
    def __init__(self, path: str):
        self.names = os.listdir(path)
        for i in self.names:
            if not ".jpg" in i:
                self.names.remove(i)
        self.limit = len(self.names)
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.names[self.counter - 1]
        else:
            raise StopIteration

def run_3(class_name, dst):
    print(3)
    tmp = create_dir(dst)
    create_dir_copy_randNames(class_name, tmp)
