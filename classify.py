# Script to classify an instance of speech data
# Uses multiple other scripts:
#	pitch.py 					- generate pitch value of speech using autocorrelation
# 	spectrogram_generator.py 	- generate spectrogram of speech
#
# File pass in file path to audio

import pitch as p
import spectrogram_generator as sg

def main(speech_file):
	threshold_f0 = 180 # 
	segment_size = 50000; # number of samples in each segment
	pitch = p.average_pitch(speech_file)
	
	if pitch < threshold: # Use female classifer
		classifier = "female classifier"
	else:
		classifier = "male classifier"
		
	spectrogram_location = sg.main(speech_file, segment_size)
	
	# Perform classification of each spectrogram 
	files = glob.glob(wavfile_location + "*.png")
	
	for file in files:
		[path, name] = os.path.split(file)
		[name, ext] = os.path.splitext(name)
		

if __name__ == "__main__" : 
	main(sys.argv[1])
