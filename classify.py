# Script to classify an instance of speech data
# Uses multiple other scripts:
#	pitch.py 					- generate pitch value of speech using autocorrelation
# 	spectrogram_generator.py 	- generate spectrogram of speech
#
# File pass in file path to audio

import os
import sys
import glob
import pylab
import errno
import wave
import datetime
import pitch as p
import spectrogram_generator_one_segment as sg
import label_image as li

female_classifier = '/home/aoife/tf_files/female_classifier' # location of female_classifier ***DO NOT CHANGE***
male_classifier = '/home/aoife/tf_files/male_classifier' # location of male_classifier ***DO NOT CHANGE***


def main(speech_file_location):
	[path, name] = os.path.split(speech_file_location)
	[name, ext] = os.path.splitext(name)
	
	spectrogram_location = create_spectrogram_location(path)
	classifications = [] # empty list to store classification values
	
	threshold_f0 = 180 # 
	segment_size = 50000; # number of samples in each segment
	speech, frame_rate = get_wav_file(speech_file_location) # Read speech file and get frame rate
	print("frame rate: " + str(frame_rate))
	
	segment_number = 1
	for i in range(0, len(speech)-segment_size, segment_size):
		pitch = p.average_pitch(speech[i:i+segment_size], frame_rate)
		print("pitch is:")
		print pitch
		sg.main(speech_file_location, speech[i:i+segment_size], spectrogram_location) # Create Spectrogram for this segment
	
		if pitch > threshold_f0: # Use female classifer
			print ("Female Voice detected in file " + name)
			classifier = "female classifier"
			# perform classification using this classifier and 'spectrogram_location'(system call??)
			classification = li.classify_image((spectrogram_location + "/" + name + ".jpg"), female_classifier)

		else:
			print ("Male Voice detected in file " + name)
			classifier = "male classifier"
			# perform classification using this classifier and 'spectrogram_location'(system call??)
			classification = li.classify_image((spectrogram_location + "/" + name + ".jpg"), male_classifier)
			
		classifications.append(classification)
		print classifications
	
	print("Classification of file " + name + " finished")
	
def create_spectrogram_location(location):
	try:
		location = location + "/spectrograms"
		os.makedirs(location) # Will create the directory if it doesn't exist
	
	except OSError as exception: # If an error is raised telling us the directory exists (from previous run) ignore
		if exception.errno != errno.EEXIST: # Raise all other errors
			raise
	
	datestr = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
	test_location = location + "/" + datestr + "TestData"
	os.makedirs(test_location) # Make unique directory for results of this test
	return test_location # Return unique file path 

def get_wav_file(file_location):
	wav = wave.open(file_location, 'r') # Open the file at 'file_location' in read-only mode
	frames = wav.readframes(-1)
	speech = pylab.fromstring(frames, 'Int16')
	frame_rate = wav.getframerate()
	wav.close()
	return speech, frame_rate

if __name__ == "__main__" : 
	print("hello")
	main(sys.argv[1])
