# 	Aoife McDonagh
# 	13411348
# 
# 	Spectrogram Generator
#
#	Input parameters
#		1. wavfile_location: path to directory containing all wav files for spectrogram creation
#		2. speech_segment: the samples in the wav file to create spectrogram of
#


import os
import errno
import sys
from scipy import *
from numpy import *
import pylab
import scikits.audiolab as audiolab
import matplotlib.pyplot as plt
import struct
import datetime
import glob
import wave

# Creates spectrogram of 'speech_segment' and stores it in 'spectrogram_location'
def create_spectrogram(speech_segment, spectrogram_location, name):
	spectrogram = plt.specgram(speech_segment) # Creating spectrogram
	plt.axis('off')
	plt.savefig(spectrogram_location + "/" + name + ".jpg", bbox_inches = 'tight', pad_inches = 0)

	
def get_wav_file(file_location):
	wav = wave.open(file_location, 'r') # Open the file at 'file_location' in read-only mode
	frames = wav.readframes(-1)
	speech = pylab.fromstring(frames, 'Int16')
	frame_rate = wav.getframerate()
	wav.close()
	return speech, frame_rate
	
# Option to specify where spectrograms are stored. 
# Otherwise folder is automatically generated.
def main(wavfile_path, speech_segment, spectrogram_location):
	[wavfile_folder, name] = os.path.split(wavfile_path)
	[name, ext] = os.path.splitext(name)
	
	create_spectrogram(speech_segment, spectrogram_location, name)
	
	
if __name__ == "__main__" : # File called standalone
	main(sys.argv[1], sys.argv[2])                                                               
#else:	# File called from another module
	
	
