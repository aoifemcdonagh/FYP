# Aoife McDonagh
# 13411348
#
# Python script for determining the pitch of audio sample

# Function to extract the pitch period from an audio sample
# Parameters:
#		sequence: autocorrelation function for the audio frame
#		min_lag: minimum number of lag samples rounded up to the nearest integer
def extractT0(sequence, minlag):
	peak, peak_location = 0;
	
	for i in range(0:len(sequence)-1):
		if sequence(i) > peak:
			peak = sequence(i)
			peak_location = i
	
	T0 = peak_location + minlag
	return T0


# Function to calculate the autocorrelation function for a given frame of audio
# Parameters:
#		filtered_speech: low pass filtered speech frame
#		minlag: minimum number of lag samples rounded up to the nearest integer
#		maxlag: maximum number of lag samples rounded up to the nearest integer
def xcorr(filtered_speech, minlag, maxlag):
	frame_size = len(speech)
	num_lags = maxlag - minlag + 1
	
	for i in range(1:num_lags-1):
		k = i + minlag - 1 # lag value
		sequence[i] = sum(abs(frame(0:frame_size-k-1).dot(frame(1+k:frame_size-1)))
		sequence[i] = sequence[i]/(frame_size-k)
		
	return sequence

	
# Function to return the pitch period value of a 32ms *frame* of speech 
def get_pitch_freq(frame, frame_rate):
	Ts = 1/frame_rate # Sample period of 'speech' (s)
	
	# Assume a pitch range of 80-260Hz
	min_f0 = 80
	max_f0 = 260
	min_lag = ceil((1/max_f0)/Ts);   # Min # of lag samples rounded up to nearest integer
	max_lag = ceil((1/min_f0)/Ts);   # Max # of lag samples rounded up to nearest integer
	
	# Get pitch value
	
	sequence = xcorr(speech, min_lag, max_lag)
	
	sequence_sum = 0;
	# Add sequence values from frame
	for i in range(0, len(sequence))
		sequence_sum = sequence_sum + sequence[i]
		
	T0 = extractT0(sequence, min_lag)
	pitch_frequency = 1/(T0*Ts)
	
	
# Split speech into 32ms frames
# get pitch of each 32ms frame
# returns average pitch value of *entire speech sample*
# best to have speech signal not be too long that pitch changes dramatically  
def average_pitch(speech):
	
	pitch_values = [] # Create an empty list for storing pitch values for averaging later
	frame_number = 0;
	
	for j in range(0, (len(speech) - frame_size) , frame_size):
		pitch = get_pitch_freq(speech[j:j+frame_size])
		pitch_values[frame_number] = pitch
		frame_number = frame_number + 1
		
	average_pitch = # sum all values in list and divide by its length to get average pitch value over entire sample
	
	return average_pitch
	
	

	



