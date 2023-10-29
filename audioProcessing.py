
import numpy as np
import scipy.io.wavfile as wavfile


#for i in range(0,180+1,5):
    # import audio wav file
#    path_load = 'data_pre/measurement_2k_no_noise_0_180_5deg/' + str(i) + '_deg.wav'
#    fs, sig = wavfile.read(path_load)
    #save only the first 10 seconds of the audio file and only the first 9 channels
#    sig = sig[0:fs*10,0:9]
    # save the audio file
#    path_save = 'data/measurement_2k_no_noise_0_180_5deg/' + str(i) + '_deg.wav'
#    wavfile.write(path_save, fs, sig)

path_load = 'data_pre/measurement_2k_noise_high_amplitude_speach_signal/speach_reference_20_deg.wav'
fs, sig = wavfile.read(path_load)
    #save only the first 10 seconds of the audio file and only the first 9 channels
sig = sig[0:fs*10,0:8]
    # save the audio file
path_save = 'data/measurement_2k_noise_high_amplitude_speach_signal/speach_reference_20_deg.wav'
wavfile.write(path_save, fs, sig)