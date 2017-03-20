# Aoife McDonagh
# 13411348
# 
# Spectrogram Generator

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

# Iterates through wav files in 'wavfile_location'
# Generates spectrograms for all segments (of size segment_size) of each
# file in wavfile_location directory
def create_spectrograms(wavfile_location, spectrogram_location, segment_size):
	#segment_size = 50000
	files = glob.glob(wavfile_location + "*.wav")
	
	for file in files:
		[path, name] = os.path.split(file)
		[name, ext] = os.path.splitext(name)
		
		speech = audiolab.sndfile(file,'read') # Read wav file 
		sound_info = speech.read_frames(speech.get_nframes()) # Extract sound info
		
		for i in range(0, (len(sound_info) - segment_size), segment_size): # Iterate through until EOF
			spectrogram = plt.specgram(sound_info[i : i + segment_size])
			pylab.savefig(spectrogram_location + "/" + name + "_" + str(i+segment_size) + ".png")
			
		speech.close()

		
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

	
# Option to specify where spectrograms are stored. 
# Otherwise folder is automatically generated.
def main(wavfile_location, segment_size):
	if len(sys.argv) > 2: # If spectrogram location has been specified
		spectrogram_location = sys.argv[2]
	else:
		spectrogram_location = create_folder(wavfile_location) # automatically generate spectrogram_location
	
	create_spectrograms(wavfile_location, spectrogram_location, segment_size)
	return spectrogram_location
	
	
if __name__ == "__main__" : # File called standalone
	main(sys.argv[1], sys.arg[2])
#else:	# File called from another module
	
	
