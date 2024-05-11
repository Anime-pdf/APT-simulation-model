import scipy.signal as scs

def apply_lowpass_filter(signal, Fs):
    return scs.lfilter(scs.firwin(101, 2400, fs=Fs),[1],signal)