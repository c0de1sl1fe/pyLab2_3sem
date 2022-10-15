import os
import random

import shutil

def create_dir_copy_randNames(class_name: str, dst:str) -> None:
    '''Create array with rand num in 0 to 10000 length of names in source dir 
    and copy with that names to dst dir'''

    path = os.path.join("dataset", class_name)
    names = os.listdir(path)
    for i in names:
        if not ".jpg" in i:
            names.remove(i)
    tmp = random.sample(range(1, 10001), len(names))
    for i in len(names):
        s = os.path.join(os.path.join('dataset', class_name), names[i])
        d = os.path.join(dst, f'{tmp[i]}.jpg')
        shutil.copy2(s, d)

def create_dir(path: str) -> str:
    '''this function create 'dataset' directory
     in path gived by user
     and return path of new_dataset dir'''
    if not os.path.isdir(os.path.join(path, 'dataset')):
        os.mkdir(os.path.join(path, 'dataset'))
    return os.path.join(path, 'dataset')



def run_3():
    print(3)