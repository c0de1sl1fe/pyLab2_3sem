import os
import csv

import tqdm


def create_csv(path_dir: str) -> None:
    '''It function collect all filenames in dir and create csv file with abs path relative path and class name in cols'''
    path = os.path.join("dataset", path_dir)
    names = os.listdir(path)
    with open(os.path.join(path, f"{path_dir}annotation.csv"), 'w') as file_csv:
        # writer = csv.writer(file_csv)
        for i in names:
            if not ".jpg" in i:
                names.remove(i)
        with tqdm.tqdm(range(len(names))) as pbar:
            for i in names:
                # writer.writerow(str(os.path.abspath(i) + "," + os.path.join(path, i) + "," + path_dir))
                file_csv.write(os.path.abspath(i) + "," +
                               os.path.join(path, i) + "," + path_dir)
                file_csv.write("\n")
                pbar.update(1)

    file_csv.close


def run_1(name: str) -> None:
    '''this function just run primary create_csv'''
    create_csv(name)
