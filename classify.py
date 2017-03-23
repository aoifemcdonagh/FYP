# Script to classify an instance of speech data
# Uses multiple other scripts:
#	pitch.py 					- generate pitch value of speech using autocorrelation
# 	spectrogram_generator.py 	- generate spectrogram of speech
#
# File pass in file path to audio

import os
import sys
import pitch as p
import spectrogram_generator as sg
import wave

def main(speech_file):
	[path, name] = os.path.split(file)
	[name, ext] = os.path.splitext(name)
	classifications = [] # empty list to store classification values
	segment_number = 0
	
	threshold_f0 = 180 # 
	segment_size = 50000; # number of samples in each segment
	speech, frame_rate = get_wav_file(speech_file) # Read speech file and get frame rate
	
	for i in range(0, len(speech_file)-segment_size, segment_size):
		pitch = p.average_pitch(speech_file[i:i+segment_size], frame_rate)
		spectrogram_location = sg.main(speech_file[i:i+segment_size], segment_size) # Create Spectrogram for this segment
	
		if pitch < threshold: # Use female classifer
			classifier = "female classifier"
			# perform classification using this classifier and 'spectrogram_location'(system call??)
			classification # = result of classification

		else:
			classifier = "male classifier"
			# perform classification using this classifier and 'spectrogram_location'(system call??)
			classification # = result of classification
			
			
		classifications[segment_number] = classification
		segment_number = segment_number + 1
		

def get_wav_file(file_location):
	wav = wave.open(file_location, 'r') # Open the file at 'file_location' in read-only mode
	frames = wav.readframes(-1)
	speech = pylab.fromstring(frames, 'Int16')
	frame_rate = wav.getframerate()
	wav.close()
	return speech, frame_rate

if __name__ == "__main__" : 
	main(sys.argv[1])
