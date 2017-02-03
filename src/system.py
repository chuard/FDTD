import numpy as np
import scipy.constants as const

class System:
    def __init__(self, cfg):



        # initialize mesh
        self.n = cfg['MESH'].getint('N')
        self.m_hx = np.zeros((self.n,self.n), dtype=np.float64)
        self.m_hy = np.zeros_like(self.m_hx)
        self.m_ez = np.zeros_like(self.m_hx)
        self.m_hx_new = np.zeros_like(self.m_hx)
        self.m_hy_new = np.zeros_like(self.m_hx)
        self.m_ez_new = np.zeros_like(self.m_hx)

        self.dt = cfg['RUN'].getfloat('dt')
        self.dx = cfg['MESH'].getfloat('L')/self.n
        self.t  = 0


    def step(self):
        dt = self.dt
        dx = self.dx
        kxy = dt/dx
        m_hx = self.m_hx
        m_hy = self.m_hy
        m_ez = self.m_ez
        mu0 = 1.25663706e-6
        e0  = 8.854187817e-12
        a   = e0/dt
        b   = e0/dt

        m_hx[:-1,:-1]   -= dt/mu0/dx*(m_ez[:-1,1:] - m_ez[:-1,:-1])
        m_hy[:-1,:-1]   += dt/mu0/dx*(m_ez[1:,:-1] - m_ez[:-1,:-1])
        m_ez[1:-1,1:-1] += 1/dx/b*(m_hy[1:-1,1:-1] - m_hy[:-2,1:-1]) - \
                           1/dx/b*(m_hx[1:-1,1:-1] - m_hx[1:-1,:-2])

        # scatterer
        m_ez[50:75,50:75] = 0


        # forcing
        m_ez[200,200] -= np.sin(1.e16*self.t)*np.exp(-(self.t-2.e-15)**2/1.e-31)

        self.t += dt


