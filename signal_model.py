import numpy as np

def generate_sync_A(Fs):
    T = 1/4160
    dt = 1/Fs
    t = np.arange(0,39*T,dt)
    n = len(t)
    sync_A = 11*np.ones(n)
    array_0_1 = (t >= 4*T) * (t <= 6*T) + \
    (t >= 8*T) * (t <= 10*T) + \
    (t >= 12*T) * (t <= 14*T) + \
    (t >= 16*T) * (t <= 18*T) + \
    (t >= 20*T) * (t <= 22*T) + \
    (t >= 24*T) * (t <= 26*T) + \
    (t >= 28*T) * (t <= 30*T)
    
    sync_A[array_0_1] = 244
    return sync_A