close all
clc

samplesize=10000;

[x, Fs]=audioread('U:\My Documents\4th Year\FYP\Matlab code\Odi.wav', [1 samplesize]);
y=fft(x, samplesize);
range=1:samplesize;
figure; plot(range, y);


Fs = 16000; Ts = 1/Fs;          % Sampling frequency, sampling period
time = 0:Ts:1;                % Define when sampling occurs 
                                % (sampling lasts for 0.1 secs):
Freqs = [100 1000];          % These are the frequencies of the signals
Xs = zeros(length(Freqs), length(time));
                                
for i=1:length(Freqs)           % Create one audio signal (tone) per frequency
    Xs(i,:) = cos(2*pi*Freqs(i)*time); 
end

x1 = sum(Xs);

y1=fft(x1, samplesize);
figure; plot(range, y1);