'''
* Created by Zhenia Syryanyy (Yevgen Syryanyy)
* e-mail: yuginboy@gmail.com
* Last modified: 31.08.2020
'''
from tempfile import NamedTemporaryFile
from config import *
import re
from pkg_lib.dir_and_file_operations import *


class VariablesReplacer:
    def __init__(self):
        self.full_filename = os.path.join(FEFF_SRC_DIR_PATH, 'atomic_tot.f90')
        self.do_backup = DO_BACKUP

    def create_file_copy(self):
        if self.do_backup:
            shutil.copy(self.full_filename, os.path.join(BACKUP_DIR, get_filename(self.full_filename)))

    def get_old_values_from_file(self):
        with open(self.full_filename, 'r') as f:
            for line in f:
                # print(line)
                for key, val in FEFF_VARS_DICT.items():
                    if not val.immutable:
                        if val.search_pattern in line:
                            old_params = \
                                [int(s) for s in re.findall(r"\b\d+\b", line)]
                            val.old_value = old_params[0]
                            print('s = ', line)
                            if val.old_value != val.value:
                                print('==>> Variable >> {} << will be change from {} to {}'.format(
                                    val.name,
                                    val.old_value,
                                    val.value,
                                ))

    def replace_values_in_file(self):
        with open(self.full_filename, 'r') as fin, \
                NamedTemporaryFile(dir=get_full_folder_path(self.full_filename), delete=False) as fout:
            for line in fin:
                # print(line)
                for key, val in FEFF_VARS_DICT.items():
                    if not val.immutable:
                        if val.search_pattern in line:
                            old_params = \
                                [int(s) for s in re.findall(r"\b\d+\b", line)]
                            val.old_value = old_params[0]
                            print('s = ', line)
                            if val.old_value != val.value:
                                line = val.output_string
                                print('new line: ', line)
                fout.write(line.encode('utf8'))
            # To make sure the content is written to disk at a given point, you can use file.flush
            fout.flush()
            # Note that the docs recommend to use os.fsync(fd) after invoking flush() of the file object. flush
            # clears Python's file object buffer, fsync instructs the OS to write its file system buffers
            # corresponding to the filedescriptor to disk.
            os.fsync(fout.fileno())
        os.rename(fout.name, self.full_filename)

    def do_routine(self):
        self.create_file_copy()
        self.get_old_values_from_file()
        self.replace_values_in_file()


if __name__ == '__main__':
    print('-> you run ', __file__, ' file in the main mode (Top-level script environment)')

    # ss = [("apple-12.34 ba33na fanc-14.23e-2yapple+45e5+67.56E+3",
    #        ['-12.34', '33', '-14.23e-2', '+45e5', '+67.56E+3']),
    #       ('hello X42 I\'m a Y-32.35 string Z30',
    #        ['42', '-32.35', '30']),
    #       ('he33llo 42 I\'m a 32 string -30',
    #        ['33', '42', '32', '-30']),
    #       ('h3110 23 cat 444.4 rabbit 11 2 dog',
    #        ['3110', '23', '444.4', '11', '2']),
    #       ('hello 12 hi 89',
    #        ['12', '89']),
    #       ('4',
    #        ['4']),
    #       ('I like 74,600 commas not,500',
    #        ['74,600', '500']),
    #       ('I like bad math 1+2=.001',
    #        ['1', '+2', '.001'])]
    #
    # for s, r in ss:
    #     rr = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", s)
    #     if rr == r:
    #         print('GOOD')
    #     else:
    #         print('WRONG', rr, 'should be', r)

    obj = VariablesReplacer()
    obj.create_file_copy()
    obj.get_old_values_from_file()
    obj.replace_values_in_file()

