![Linux](https://img.shields.io/badge/-Linux-grey?logo=linux)
![Usage](https://img.shields.io/badge/Usage-FEFF9%20compilation%20variable%20updater-blue)
![Python](https://img.shields.io/badge/Python-v3.6%5E-orange?logo=python)

## Index

* [Description](#description)
* [Features](#features)
* [Installation](#installation)

## Description

**FEFF9 compilation variable updater** this is a cli app for updating global variables in [FEFF9](http://feff.phys
.washington.edu/feffproject-feff.html) program fortran source files *.f90.


## Features

* Automatic changing variables.
* Automatic backup old source files.
* Separate configuration file

## Installation

### 1. Create Virtual Python Environment and Install Python3 interpreter
Additional information on https://www.python.org/downloads/
and 
[Creation of virtual environments](https://docs.python.org/3/library/venv.html)

or simple way to create subfolder venv (with python packages) inside the current directory:

    $ python -m venv venv

### 2. Clone this repository into your directory

    $ mkdir feff9_compilation_variable_updater && cd feff9_compilation_variable_updater
    
    
    $ git clone https://github.com/xyz-man/feff9_compilation_variable_updater.git
        or
    $ git clone -b develop https://github.com/xyz-man/feff9_compilation_variable_updater.git

### 3. Install requirements


    $ pip install -r requirements.txt
    
### 4. Configuration

Edit the `settings.py` file and change needed values. 
Main part of settings:

    $   # reset all values to default values:
        RESET_TO_DEFAULT = True
        
        FEFF_VARS_DICT = odict()
        # Path to feff source *.f90 files:
        FEFF_SRC_DIR_PATH = '/home/yugin/PycharmProjects/feff_vars/data/src/feff90_src/'
        # save original files:
        DO_BACKUP = True
        
Change `RESET_TO_DEFAULT` to `False` if you need to change the defaults to new ones.
Specify the path to the folder with the source codes of the `FEFF9` program:

    $   # Path to feff source *.f90 files:
        FEFF_SRC_DIR_PATH = '/opt/feff/feff90/mod/MPI/'

In block:
    
    $   # The hardcoded limit on cluster size that can NEVER be exceeded :
        nclusxhardlimit = 3000
        
        obj = FEFF_Variable()
        obj.name = 'nclusxhardlimit'
        obj.value = nclusxhardlimit
        obj.default_value = 3000
        obj.comment = ''
        obj.help_string = 'The hardcoded limit on cluster size that can NEVER be exceeded'
        obj.reset_to_default_value = RESET_TO_DEFAULT
        obj.rebuild()
        FEFF_VARS_DICT[str(obj.name)] = obj
        
you only need to change the value in the following line:

        $ nclusxhardlimit = 3000
        
the lines below describe the internal procedure of the program. 
      
### 5. Run

Inside root project directory (`.feff9_compilation_variable_updater/`) activate local virtual environments:

    $ source venv/bin/activate
    
and run main.py:

    $ python main.py
    
If you choose the `FEFF9` source directory with `root` access permissions, you can execute this Python code as the 
`root` user.

### 6. License

**FEFF9 compilation variable updater** has been created under the **GNU GPLv3 license**

 