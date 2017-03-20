# Python script for generating spectrograms

import wave
from scipy.io import wavfile
import matplotlib.pyplot as plt
import pylab

filename = "/media/sf_tensorflow_VM/audio/cleaned_files/David_1.wav"
[fs, data] = wavfile.read(filename)	# Open the file in read only mode
#frames = file.readframes(-1)
#fs = file.getframerate()
num_frames = len(data)
#speech = pylab.fromstring(frames, 'Int16')
segment_size = 50000

#for i in range(0, (num_frames - segment_size), segment_size): # Iterate through until EOF
#	pylab.figure(num=None, figsize=(19, 12))
#	pylab.subplot(111)
#	pylab.title('spectrogram of %r' % filename)
#	pylab.specgram(data[i:i+segment_size], fs)
#	pylab.savefig('spectrogram.png')

pylab.figure(num=None, figsize=(19, 12))
pylab.subplot(111)
pylab.title('spectrogram of %r' % filename)
pylab.specgram(data[segment_size:segment_size+segment_size], fs)
pylab.savefig('spectrogram.png')
