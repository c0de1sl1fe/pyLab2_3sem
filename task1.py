import os

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
        for i in names:
            # writer.writerow(str(os.path.abspath(i) + "," + os.path.join(path, i) + "," + path_dir))
            file_csv.write(os.path.abspath(i) + "," +
                           os.path.join(path, i) + "," + path_dir)
            file_csv.write("\n")
    file_csv.close


def iterator1(name: str) -> str:
    '''Just interater for direcrory'''
    names = os.listdir(os.path.join("dataset", name))
    for i in names:
        if not ".jpg" in i:
            names.remove(i)
    for i in range(len(names)):
        yield (names[i])
    return None


    # class Iterator1_img:
    #     def __init__(self, name: str):
    #         self.names = os.listdir(os.path.join("dataset", name))
    #         for i in self.names:
    #             if not ".jpg" in i:
    #                 self.names.remove(i)
    #         self.limit = len(self.names)
    #         self.counter = 0

    #     def __next__(self):
    #         if self.counter < self.limit:
    #             self.counter += 1
    #             return self.names[self.counter - 1]
    #         else:
    #             raise StopIteration
    #     def clear(self):
    #         self.counter = 0
# class Iterator1_img:
#     def __init__(self, name: str, path: str):
#         self.path = ""
#         self.names = []
#         self.limit = 0
#         self.counter = 0
#         self.init(name, path)

#     def __next__(self):
#         if self.counter < self.limit:
#             self.counter += 1
#             return self.names[self.counter - 1]
#         else:
#             raise StopIteration

#     def init(self, name: str, path: str):
#         if not "dataset" in path:
#             raise ("error")
#         self.path = path
#         # self.names = os.listdir(os.path.join("dataset", name))
#         self.names = os.listdir(os.path.join(path, name))

#         for i in self.names:
#             if not ".jpg" in i:
#                 self.names.remove(i)
#         self.limit = len(self.names)
#         self.counter = 0

#     def clear(self):
#         self.counter = 0

#     def setName(self, name: str):
#         self.init(name, self.path)
class Iterator1_img:
    def __init__(self, name: str, path: str):
        self.path = ""
        self.name = ""
        self.names = []
        self.limit = 0
        self.counter = 0
        self.init(name, path)

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.names[self.counter - 1]
        else:
            raise StopIteration

    def init(self, name: str, path: str):
        if not "dataset" in path:
            raise ("error")
        self.path = path
        self.name = name
        # self.names = os.listdir(os.path.join("dataset", name))
        self.names = os.listdir(os.path.join(self.path, self.name))

        for i in self.names:
            if not ".jpg" in i:
                self.names.remove(i)
        self.limit = len(self.names)
        self.counter = 0

    def clear(self):
        self.counter = 0

    def setName(self, name: str):
        self.init(name, self.path)

    def setPath(self, path: str):
        self.init(self.name, path)




def run_1(name: str) -> None:
    '''this function just run primary create_csv'''
    create_csv(name)
