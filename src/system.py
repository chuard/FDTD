import numpy as np
import scipy.constants as const
import stepper

def get_solver(cfg):
    stepper_sc = stepper.Stepper_base.__subclasses__()
    st = object()
    for s in stepper_sc:
        if hasattr(s,'stepper_name') and getattr(s,'stepper_name') == cfg['RUN']['STEPPER']:
            st = s

    if not hasattr(st,'stepper_name'):
        raise NameError('Stepper not found')

    solver = type("FDTD_solver",(System,st),dict())
    return solver(cfg)


class System:
    def __init__(self, cfg):

        # initialize mesh
        self.n = cfg['MESH'].getint('N')
        self.m_hx = np.zeros((self.n,self.n), dtype=np.float64, order='F')
        self.m_hy = np.zeros_like(self.m_hx, order='F')
        self.m_ez = np.zeros_like(self.m_hx, order='F')

        # initialize other stuff... should probably use dictionary.
        self.dt = cfg['RUN'].getfloat('dt')
        self.dx = cfg['MESH'].getfloat('L')/self.n
        self.nth= cfg['RUN'].getint('NTHREADS')
        self.nsteps = cfg['RUN'].getint('NSTEPS')
        self.t  = 0
        self.out_frames = 0

    def take_steps(self):

        for i in range(self.nsteps):
            self.step()
