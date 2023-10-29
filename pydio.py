import numpy as np
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt

def collectPlaneWave(N,d, theta, sig,fs, c=343):
    # returns n vectors shifted by the arrival time of the first plane wave due to the angle theta

    if theta > 90:
        angle = 180-theta
    else:
        angle = theta
    microphones = np.zeros((N,len(sig)))
    for i in range(N):
        delay = d*i*np.cos(np.radians(angle))*1/c
        
        microphones[i] = np.roll(sig,int((delay*fs)))
        
    if theta > 90:
        microphones = np.flip(microphones, axis=0)

    return microphones


def equalizationCoefficients(path):
    # ensures that all channels have the same rms value
    # returns the equalization coefficients for the microphones in the array
    # the first channel is used as reference

    fs, sig = wavfile.read(path)
    # convert to float64 to avoid overflow
    sig = sig.astype(np.float64)
    # remove the last channel
    #sig = np.delete(sig, len(sig[0])-1, axis=1)

    # make all channels equal using rms value
    rms = np.zeros((len(sig[0])))
    for i in range(len(sig[0])):
        rms[i] = np.sqrt(np.mean(sig[:,i]**2))

    # normalize using rms value to create equal channels using the first channel as reference to create coefficients
    a = np.zeros((len(sig[0])))
    for i in range((len(sig[0]))):
        a[i] = rms[0]/rms[i]
    return a

def Fn(n, d, theta):
    # assuming planar wavefront
    c = 343
    return (n)*d*np.cos(np.radians(theta))/c

def plot_cartesian(x,y, name):
    # cartesian plot
    
    plt.figure(figsize=(6,4))
    #plt.figure()
    plt.plot(x,y)
    plt.xlabel('Angle [deg]')
    plt.ylabel('Amplitude [dB]')
    plt.xlim([0, 180])
    plt.grid(True, linestyle='--')
    
    plt.savefig('plots/'+ name +'.svg')


def plot_polar(x,y, name):
    # polar plot

    plt.figure()
    plt.polar(np.radians(x), y)
    plt.ylim([-50, 0])
    plt.yticks([-10, -20,-30, -40, -50])
    plt.grid(True, linestyle='--')
    plt.xlim([0, np.radians(180)])


    plt.savefig('plots/'+ name +'.svg')

def plot_combi(x,y,name):
    # plot both polar and cartesian in a single figure
    fig = plt.figure(figsize=(12,4.5))
    
    ax = fig.add_subplot(121,aspect=0.95)
    ax.plot(x,y)
    ax.set_xlabel('Angle [deg]')
    ax.set_ylabel('Amplitude [dB]')
    ax.set_xlim([0, 180])
    ax.set_ylim([-80, 0])
    #ax.set_yticks([-10, -20,-30, -40, -50])
    #ax.set_xticks([0, 20, 40, 60, 80, 100, 120, 140, 160, 180])
    ax.grid(True, linestyle='--')

    ax = fig.add_subplot(122, projection='polar')
    ax.plot(np.radians(x), y)
    ax.set_ylim([-50, 0])
    ax.set_yticks([-10, -20,-30, -40, -50])
    ax.grid(True, linestyle='--')
    ax.set_xlim([0, np.radians(180)])

    plt.tight_layout()
    plt.savefig('plots/'+ name +'.svg',bbox_inches='tight', pad_inches=0)


