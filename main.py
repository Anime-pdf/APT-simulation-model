import numpy as np
from matplotlib import pyplot as plt

# signal model
from signal_model import generate_sync_A

# lowpass filter
from lowpass_filter import apply_lowpass_filter

# entry point
def main():
    Fs = 11025
    so = generate_sync_A(Fs)
    
    n = len(so)
    zero_samples = np.zeros(n)
    s = np.concatenate( (zero_samples, so, zero_samples) ) # widen it a bit
    t = np.arange(len(s)) * 1/Fs
    
    plt.figure()
    plt.title('Clean signal')
    plt.plot(t, s)
    
    s = apply_lowpass_filter(s, Fs)
    
    plt.figure()
    plt.title('Signal with lowpass filter')
    plt.plot(t, s)
    
if __name__ == "__main__":
    main()