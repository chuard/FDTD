#!/uigelh_dua2/chuard/anaconda3/bin/python

import sys
from inifile import Inifile

def main(arg):
    print(arg)
    cfg = Inifile.load(arg)
    print(cfg)

if __name__ == '__main__':
    print(sys.argv[:])
    main(sys.argv)
