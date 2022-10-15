import os
import shutil


def create_dir(path: str) -> str:
    '''this function create 'dataset' directory
     in path gived by user
     and return path of new_dataset dir'''
    if not os.path.isdir(os.path.join(path, 'dataset')):
        os.mkdir(os.path.join(path, 'dataset'))
    return os.path.join(path, 'dataset')


def copy_dataset(class_name_copy: str, dst: str) -> None:
    '''copy all files in class_name_copy directory in data set to dst'''
    for item in os.listdir(os.path.join('dataset', class_name_copy)):
        if ".jpg" in item:
            s = os.path.join(os.path.join('dataset', class_name_copy), item)
            d = os.path.join(dst, f'{class_name_copy}_{item}')
            shutil.copy2(s, d)


def run_2(new_path_dir, name_class):
    '''main function, that toggle all realWorking functions'''
    new_dataset_path = create_dir(new_path_dir)
    copy_dataset(name_class, new_dataset_path)
