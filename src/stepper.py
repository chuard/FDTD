import numpy as np
import update

class Stepper_base:
    def __init__(self, cfg):
        pass

    def step(self):

        # bulk update
        self.update()

        # add scatterer
        self.m_ez[50:75,50:75] = 0

        # add forcing
        self.m_ez[200,200] -= np.sin(1.e16*self.t)*np.exp(-(self.t-2.e-15)**2/1.e-31)
#       self.m_ez[200,200] -= np.sin(1.e16*self.t)

        # update system time
        self.t += self.dt

class Stepper_fort(Stepper_base):
    stepper_name = 'fortran'

    def update(self):
        dt,dx = self.dt,self.dx
        m_hx,m_hy,m_ez = self.m_hx,self.m_hy,self.m_ez

        m_hy,m_hx,m_ez = update.update(m_hy,m_hx,m_ez,dx,dt,self.nth)

class Stepper_py(Stepper_base):
    stepper_name = 'python'

    def update(self):
        mu0 = 1.25663706e-6
        e0  = 8.854187817e-12
        dt,dx = self.dt,self.dx
        m_hx,m_hy,m_ez = self.m_hx,self.m_hy,self.m_ez
        a   = e0/dt
        b   = e0/dt

        m_hx[:-1,:-1]   -= dt/mu0/dx*(m_ez[:-1,1:] - m_ez[:-1,:-1])
        m_hy[:-1,:-1]   += dt/mu0/dx*(m_ez[1:,:-1] - m_ez[:-1,:-1])
        m_ez[1:-1,1:-1] += 1/dx/b*(m_hy[1:-1,1:-1] - m_hy[:-2,1:-1]) - \
                           1/dx/b*(m_hx[1:-1,1:-1] - m_hx[1:-1,:-2])
