'''
* Created by Zhenia Syryanyy (Yevgen Syryanyy)
* e-mail: yuginboy@gmail.com
* Last modified: 30.08.2020
'''
from pkg_lib.bases import FEFF_Variable
from collections import OrderedDict as odict
from pkg_lib.dir_and_file_operations import create_out_data_folder


# reset all values to default values:
RESET_TO_DEFAULT = True

FEFF_VARS_DICT = odict()
# Path to feff source *.f90 files:
FEFF_SRC_DIR_PATH = '/home/yugin/PycharmProjects/feff_vars/data/src/feff90_src/'
# save original files:
DO_BACKUP = True

if DO_BACKUP:
    BACKUP_DIR = create_out_data_folder(FEFF_SRC_DIR_PATH, 'backup')

'''
! The hardcoded limit on cluster size that can NEVER be exceeded :
  integer, parameter :: nclusxhardlimit = 3000
! The hardcoded upper limit on l-values that can NEVER be exceeded :
  integer, parameter :: lxhardlimit = 20
! The hardcoded upper limit on the number of potentials that can NEVER be exceeded :
  integer, parameter :: nphxhardlimit = 31
  private dimFName, lxhardlimit, nclusxhardlimit !! Meaning no other code can change these ...

  integer,parameter :: nclxtd = 100     ! Maximum number of atoms for tdlda module.
  integer,parameter :: nspx   = 1       ! Max number of spins: 1 for spin average; 2 for spin-dep
  integer,parameter :: natx   = 4000    ! Max number of atoms in problem for the pathfinder and ffsort
  integer,parameter :: nattx  = 4000    ! Max number of atoms in problem for the rdinp
  integer,parameter :: nphx   = 14      ! Max number of unique potentials (potph)
  integer,parameter :: ltot   = 24      ! Max number of ang mom (arrays 1:ltot+1)
  integer,parameter :: nrptx  = 1251    ! Loucks r grid used through overlap and in phase work arrays
  integer,parameter :: nex    = 500     ! Number of energy points genfmt, etc.
  integer,parameter :: lamtot = 15      ! Max number of distinct lambda's for genfmt 15 handles iord 2 and exact ss
  integer,parameter :: mtot   = 4       ! Vary mmax and nmax independently
  integer,parameter :: ntot   = 2 
  integer,parameter :: npatx  = 8       ! Max number of path atoms, used  in path finder, NOT in genfmt
  integer,parameter :: legtot = npatx+1 ! Matches path finder, used in GENFMT
  integer,parameter :: novrx  = 8       ! Max number of overlap shells (OVERLAP card)
  integer,parameter :: nheadx = 20+nphxhardlimit      ! Max number of header lines !KJ 7-09 added term to accomodate large systems in xsect.bin header
  integer,parameter :: MxPole = 1000    ! Max number of poles that can be used to model epsilon^-1 for HL multipole self energy
  integer,parameter :: nwordx = max(100,2+2*nphxhardlimit)     ! An infuriatingly stupid parameter that shows up in a few places. KJ added 7-09.  used to be 20 - must be at least 2*(1+nphx) for feff.bin header.
  integer,parameter :: novp = 40 ! For istprm, movrlp, ovp2mt - an atom list cutoff that should be high enough to include one atom of each potential type.  Added 2-2011 !KJ
'''
# The hardcoded limit on cluster size that can NEVER be exceeded :
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

# The hardcoded upper limit on l-values that can NEVER be exceeded :
lxhardlimit = 20

obj = FEFF_Variable()
obj.name = 'lxhardlimit'
obj.value = lxhardlimit
obj.default_value = 20
obj.comment = ''
obj.help_string = 'The hardcoded upper limit on l-values that can NEVER be exceeded'
obj.reset_to_default_value = RESET_TO_DEFAULT
obj.rebuild()
FEFF_VARS_DICT[str(obj.name)] = obj


# The hardcoded upper limit on the number of potentials that can NEVER be exceeded :
nphxhardlimit = 31

obj = FEFF_Variable()
obj.name = 'nphxhardlimit'
obj.value = nphxhardlimit
obj.default_value = 31
obj.comment = ''
obj.help_string = 'The hardcoded upper limit on the number of potentials that can NEVER be exceeded'
obj.reset_to_default_value = RESET_TO_DEFAULT
obj.rebuild()
FEFF_VARS_DICT[str(obj.name)] = obj

# Maximum number of atoms for tdlda module.
nclxtd = 100

obj = FEFF_Variable()
obj.name = 'nclxtd'
obj.value = nclxtd
obj.default_value = 100
obj.comment = 'Maximum number of atoms for tdlda module'
obj.help_string = 'Maximum number of atoms for tdlda module'
obj.reset_to_default_value = RESET_TO_DEFAULT
obj.rebuild()
FEFF_VARS_DICT[str(obj.name)] = obj


# Max number of spins: 1 for spin average; 2 for spin-dep:
nspx   = 1

obj = FEFF_Variable()
obj.name = 'nspx'
obj.value = nspx
obj.default_value = 1
obj.comment = 'Max number of spins: 1 for spin average; 2 for spin-dep'
obj.help_string = 'Max number of spins: 1 for spin average; 2 for spin-dep'
obj.reset_to_default_value = RESET_TO_DEFAULT
obj.rebuild()
FEFF_VARS_DICT[str(obj.name)] = obj


# Max number of atoms in problem for the pathfinder and ffsort:
natx   = 4000

obj = FEFF_Variable()
obj.name = 'natx'
obj.value = natx
obj.default_value = 4000
obj.comment = 'Max number of atoms in problem for the pathfinder and ffsort'
obj.help_string = 'Max number of atoms in problem for the pathfinder and ffsort'
obj.reset_to_default_value = RESET_TO_DEFAULT
obj.rebuild()
FEFF_VARS_DICT[str(obj.name)] = obj


# Max number of atoms in problem for the rdinp:
nattx  = 4000

obj = FEFF_Variable()
obj.name = 'nattx'
obj.value = nattx
obj.default_value = 4000
obj.comment = 'Max number of atoms in problem for the rdinp'
obj.help_string = 'Max number of atoms in problem for the rdinp'
obj.reset_to_default_value = RESET_TO_DEFAULT
obj.rebuild()
FEFF_VARS_DICT[str(obj.name)] = obj


# Max number of unique potentials (potph):
nphx   = 14

obj = FEFF_Variable()
obj.name = 'nphx'
obj.value = nphx
obj.default_value = 14
obj.comment = 'Max number of unique potentials (potph)'
obj.help_string = 'Max number of unique potentials (potph)'
obj.reset_to_default_value = RESET_TO_DEFAULT
obj.rebuild()
FEFF_VARS_DICT[str(obj.name)] = obj


# Max number of ang mom (arrays 1:ltot+1):
ltot   = 24

obj = FEFF_Variable()
obj.name = 'ltot'
obj.value = ltot
obj.default_value = 24
obj.comment = 'Max number of ang mom (arrays 1:ltot+1)'
obj.help_string = 'Max number of ang mom (arrays 1:ltot+1)'
obj.reset_to_default_value = RESET_TO_DEFAULT
obj.rebuild()
FEFF_VARS_DICT[str(obj.name)] = obj


# Loucks r grid used through overlap and in phase work arrays:
nrptx  = 1251

obj = FEFF_Variable()
obj.name = 'nrptx'
obj.value = nrptx
obj.default_value = 1251
obj.comment = 'Loucks r grid used through overlap and in phase work arrays'
obj.help_string = 'Loucks r grid used through overlap and in phase work arrays'
obj.reset_to_default_value = RESET_TO_DEFAULT
obj.rebuild()
FEFF_VARS_DICT[str(obj.name)] = obj


# Number of energy points genfmt, etc.:
nex    = 500

obj = FEFF_Variable()
obj.name = 'nex'
obj.value = nex
obj.default_value = 500
obj.comment = 'Number of energy points genfmt, etc.'
obj.help_string = 'Number of energy points genfmt, etc.'
obj.reset_to_default_value = RESET_TO_DEFAULT
obj.rebuild()
FEFF_VARS_DICT[str(obj.name)] = obj


# Max number of distinct lambda's for genfmt 15 handles iord 2 and exact ss:
lamtot = 15

obj = FEFF_Variable()
obj.name = 'lamtot'
obj.value = lamtot
obj.default_value = 15
obj.comment = "Max number of distinct lambda's for genfmt 15 handles iord 2 and exact ss"
obj.help_string = "Max number of distinct lambda's for genfmt 15 handles iord 2 and exact ss"
obj.reset_to_default_value = RESET_TO_DEFAULT
obj.rebuild()
FEFF_VARS_DICT[str(obj.name)] = obj


# Vary mmax and nmax independently:
mtot   = 4

obj = FEFF_Variable()
obj.name = 'mtot'
obj.value = mtot
obj.default_value = 4
obj.comment = 'Vary mmax and nmax independently'
obj.help_string = 'Vary mmax and nmax independently'
obj.reset_to_default_value = RESET_TO_DEFAULT
obj.rebuild()
FEFF_VARS_DICT[str(obj.name)] = obj


ntot   = 2

obj = FEFF_Variable()
obj.name = 'ntot'
obj.value = ntot
obj.default_value = 2
obj.comment = 'Vary mmax and nmax independently'
obj.help_string = 'Vary mmax and nmax independently'
obj.reset_to_default_value = RESET_TO_DEFAULT
obj.rebuild()
FEFF_VARS_DICT[str(obj.name)] = obj


# Max number of path atoms, used  in path finder, NOT in genfmt:
npatx  = 8

obj = FEFF_Variable()
obj.name = 'npatx'
obj.value = npatx
obj.default_value = 8
obj.comment = 'Max number of path atoms, used  in path finder, NOT in genfmt'
obj.help_string = 'Max number of path atoms, used  in path finder, NOT in genfmt'
obj.reset_to_default_value = RESET_TO_DEFAULT
obj.rebuild()
FEFF_VARS_DICT[str(obj.name)] = obj


# Matches path finder, used in GENFMT:
legtot = npatx+1

obj = FEFF_Variable()
obj.name = 'legtot'
obj.value = legtot
obj.default_value = 'npatx+1'
obj.comment = 'Matches path finder, used in GENFMT'
obj.help_string = 'Matches path finder, used in GENFMT'
obj.reset_to_default_value = RESET_TO_DEFAULT
obj.rebuild()
obj.immutable = True  # Variable will not change
FEFF_VARS_DICT[str(obj.name)] = obj


# Max number of overlap shells (OVERLAP card):
novrx  = 8

obj = FEFF_Variable()
obj.name = 'novrx'
obj.value = novrx
obj.default_value = 8
obj.comment = 'Max number of overlap shells (OVERLAP card)'
obj.help_string = 'Max number of overlap shells (OVERLAP card)'
obj.reset_to_default_value = RESET_TO_DEFAULT
obj.rebuild()
FEFF_VARS_DICT[str(obj.name)] = obj


# Max number of header lines !KJ 7-09 added term to accomodate large systems in xsect.bin header:
nheadx = 20+nphxhardlimit

obj = FEFF_Variable()
obj.name = 'nheadx'
obj.value = nheadx
obj.default_value = '20+nphxhardlimit'
obj.comment = 'Max number of header lines !KJ 7-09 added term to accomodate large systems in xsect.bin header'
obj.help_string = 'Max number of header lines !KJ 7-09 added term to accomodate large systems in xsect.bin header'
obj.reset_to_default_value = RESET_TO_DEFAULT
obj.rebuild()
obj.immutable = True  # Variable will not change
obj.immutable = False  # Variable will not change
FEFF_VARS_DICT[str(obj.name)] = obj


# Max number of poles that can be used to model epsilon^-1 for HL multipole self energy:
MxPole = 10001

obj = FEFF_Variable()
obj.name = 'MxPole'
obj.value = MxPole
obj.default_value = 1000
obj.comment = 'Max number of poles that can be used to model epsilon^-1 for HL multipole self energy'
obj.help_string = 'Max number of poles that can be used to model epsilon^-1 for HL multipole self energy'
obj.reset_to_default_value = RESET_TO_DEFAULT
obj.rebuild()
FEFF_VARS_DICT[str(obj.name)] = obj


# An infuriatingly stupid parameter that shows up in a few places. KJ added 7-09.  used to be 20 - must be at
# least 2*(1+nphx) for feff.bin header.:
nwordx = max(100, 2+2*nphxhardlimit)

obj = FEFF_Variable()
obj.name = 'nwordx'
obj.value = nwordx
obj.default_value = 'max(100, 2+2*nphxhardlimit)'
obj.comment = 'An infuriatingly stupid parameter that shows up in a few places. KJ added 7-09.  used to be 20 - must ' \
              'be at least 2*(1+nphx) for feff.bin header.'
obj.help_string = obj.comment
obj.reset_to_default_value = RESET_TO_DEFAULT
obj.rebuild()
obj.immutable = True  # Variable will not change
FEFF_VARS_DICT[str(obj.name)] = obj


# For istprm, movrlp, ovp2mt - an atom list cutoff that should be high enough to include one atom of each potential
# type.  Added 2-2011 !KJ:
novp = 401

obj = FEFF_Variable()
obj.name = 'novp'
obj.value = novp
obj.default_value = 40
obj.comment = 'For istprm, movrlp, ovp2mt - an atom list cutoff that should be high enough to include one atom of ' \
              'each potential type.  Added 2-2011 !KJ'
obj.help_string = obj.comment
obj.reset_to_default_value = RESET_TO_DEFAULT
obj.rebuild()
FEFF_VARS_DICT[str(obj.name)] = obj


if __name__ == '__main__':
    print('-> you run ', __file__, ' file in the main mode (Top-level script environment)')
    print(FEFF_VARS_DICT)
    print(FEFF_VARS_DICT)
