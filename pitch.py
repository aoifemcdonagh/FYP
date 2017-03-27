# Aoife McDonagh
# 13411348
#
# Python script for determining the pitch of audio sample

# Function to extract the pitch period from an audio sample
# Parameters:
#		sequence: autocorrelation function for the audio frame
#		min_lag: minimum number of lag samples rounded up to the nearest integer

from numpy import dot

def extractT0(sequence, minlag):
	peak = 0 
	peak_location = 0
	
	for i in range(0, len(sequence)-1):
		if sequence[i] > peak:
			peak = sequence[i]
			peak_location = i
	
	T0 = peak_location + minlag
	return T0


# Function to calculate the autocorrelation function for a given frame of audio
# Parameters:
#		filtered_speech: low pass filtered speech frame
#		minlag: minimum number of lag samples rounded up to the nearest integer
#		maxlag: maximum number of lag samples rounded up to the nearest integer
def xcorr(frame, minlag, maxlag):
	frame_size = len(frame)
	num_lags = maxlag - minlag
	
	sequence = []
	for i in range(0, num_lags):
		k = i + minlag - 2 # lag value
		#sequence[i] = sum(abs(frame[0:frame_size-k-1].dot(frame[k:frame_size-1])))
		sequence_value_i = dot(frame[0:(frame_size-1)-k], frame[k:frame_size-1])
		sequence_value_i = (sequence_value_i/(frame_size-k))
		
		sequence.append(sequence_value_i)
	
	return sequence
		
# Function to return the pitch period value of a 32ms *frame* of speech 
def get_pitch_freq(frame, frame_rate):
	Ts = 1.0/frame_rate # Sample period of 'speech' (s)
	# Assume a pitch range of 80-260Hz
	min_f0 = 80
	max_f0 = 260
	min_lag = int(round((1.0/max_f0)/Ts));   # Min # of lag samples rounded up to nearest integer
	max_lag = int(round((1.0/min_f0)/Ts));   # Max # of lag samples rounded up to nearest integer
	# Get pitch value
	sequence = xcorr(frame, min_lag, max_lag)
	T0 = extractT0(sequence, min_lag)
	pitch_frequency = 1.0/(T0*Ts)
	return pitch_frequency
	
	
# Split speech into 32ms frames
# get pitch of each 32ms frame
# returns average pitch value of *entire speech sample*
# best to have speech signal not be too long that pitch changes dramatically  
def average_pitch(speech, frame_rate):
	frame_size = int(frame_rate*0.032) # 32ms
	pitch_values = [] # Create an empty list for storing pitch values for averaging later
	
	for j in range(0, (len(speech) - frame_size) , frame_size):
		pitch = get_pitch_freq(speech[j:j+frame_size], frame_rate) # get pitch of 32ms frame
		pitch_values.append(pitch)
		
	average_pitch = sum(pitch_values)/len(pitch_values) # sum all values in list and divide by its length to get average pitch value over entire sample
	
	return average_pitch
	
if __name__ == "__main__" : 
	print("pitch main: this should not be printed")
	average_pitch(sys.argv[1], sys.argv[2])




