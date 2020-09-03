'''
* Created by Zhenia Syryanyy (Yevgen Syryanyy)
* e-mail: yuginboy@gmail.com
* Last modified: 30.08.2020
'''
from config import *
from pkg_lib.utils import *
from pprint import pprint


class FilesReplacer:
    def __init__(self):
        self.extension = 'f90'

    def start(self):
        files_lst = full_path_list_of_filenames_with_selected_ext(FEFF_SRC_DIR_PATH, ext=self.extension)
        for fin in files_lst:
            obj = VariablesReplacer()
            obj.full_filename = fin
            obj.do_routine()


if __name__ == '__main__':
    print('-> you run ', __file__, ' file in the main mode (Top-level script environment)')
    obj = FilesReplacer()
    obj.start()

