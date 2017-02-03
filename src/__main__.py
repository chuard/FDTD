#!/uigelh_dua2/chuard/anaconda3/bin/python

import sys
import configparser
from system import System
import matplotlib.pyplot as plt
import numpy as np

def main(arg):

    # read in ini file
    cfg = configparser.ConfigParser()
    cfg.read(arg)

    s = System(cfg)
    for i in range(cfg['RUN'].getint('NSTEPS')):
        s.step()



    max_val = np.amax(np.absolute(s.m_ez))
    print(max_val)
    print(s.m_ez[0,0])
    fig = plt.figure()
    ax = fig.add_subplot(111,aspect='equal')
    plt.pcolor(s.m_ez,vmin=-max_val,vmax=max_val,cmap='RdBu_r')
    plt.show()





if __name__ == '__main__':
    main(sys.argv[1])
