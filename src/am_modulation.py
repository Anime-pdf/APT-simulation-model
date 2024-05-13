import numpy as np

def apply_am_modulation(signal, Fs, Fsub = 2.4e3):
    A_t = signal / max(signal)
    t = np.arange(len(A_t)) * 1/Fs
    return A_t * np.cos(2*np.pi*Fsub*t)