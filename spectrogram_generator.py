# 	Aoife McDonagh
# 	13411348
# 
# 	Spectrogram Generator
#
#	Input parameters
#		1. wavfile_location: path to directory containing all wav files for spectrogram creation
#		2. segment_size: size of 
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

# Iterates through wav files in 'wavfile_location'
# Generates spectrograms for all segments (of size segment_size) of each
# file in wavfile_location directory
def create_spectrograms(wavfile_location, spectrogram_location):
	segment_size = 50000
	files = glob.glob(wavfile_location + "*.wav")
	
	for file in files:
		[path, name] = os.path.split(file)
		[name, ext] = os.path.splitext(name)
		
		speech, frame_rate = get_wav_file(file) # Read wav file and get frame rate
		#sound_info = speech.read_frames(speech.get_nframes()) # Extract sound info
		
		for i in range(0, (len(speech) - segment_size - 1), segment_size): # Iterate through until EOF
			spectrogram = plt.specgram(speech[i : i + segment_size], Fs = frame_rate) # Creating spectrogram
			plt.axis('off')
			plt.savefig(spectrogram_location + "/" + name + "_" + str(i+segment_size) + ".jpg", bbox_inches = 'tight', pad_inches = 0)

		
# Function to create folders to store spectrograms in
# Returns path to directories created
# Returns path to spectrogram directories if they already exist (from previous runs)
def create_folder(location):
	try:
		location = location + "/spectrograms"
		os.makedirs(location) # Will create the directory if it doesn't exist
	
	except OSError as exception: # If an error is raised telling us the directory exists (from previous run) ignore
		if exception.errno != errno.EEXIST: # Raise all other errors
			raise
	
	datestr = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
	test_location = location + "/" + datestr
	os.makedirs(test_location) # Make unique directory for results of this test
	return test_location # Return unique file path 

	
def get_wav_file(file_location):
	wav = wave.open(file_location, 'r') # Open the file at 'file_location' in read-only mode
	frames = wav.readframes(-1)
	speech = pylab.fromstring(frames, 'Int16')
	frame_rate = wav.getframerate()
	wav.close()
	return speech, frame_rate
	
# Option to specify where spectrograms are stored. 
# Otherwise folder is automatically generated.
def main(wavfile_location):
	if len(sys.argv) > 2: # If spectrogram location has been specified
		spectrogram_location = sys.argv[2]
	else:
		spectrogram_location = create_folder(wavfile_location) # automatically generate spectrogram_location
	
	create_spectrograms(wavfile_location, spectrogram_location)
	return spectrogram_location
	
	
if __name__ == "__main__" : # File called standalone
	main(sys.argv[1])                                                               
#else:	# File called from another module
	
	
