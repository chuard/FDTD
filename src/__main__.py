#!/uigelh_dua2/chuard/anaconda3/bin/python

import sys
from inifile import Inifile
import configparser

def main(arg):

    # read in ini file
    cfg = configparser.ConfigParser()
    cfg.read(arg)

    print(cfg['not there'])



if __name__ == '__main__':
    main(sys.argv[1])
