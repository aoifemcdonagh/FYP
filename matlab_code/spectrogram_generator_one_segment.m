% Aoife McDonagh
% 13411348
% Script for creating spectograms for use in CNN
clc
clear all
close all

wav_file = 'U:\My Documents\4th Year\FYP\Irish Language\Ulaidh\Ronan-Bruscar-C1-Bliain1-2011.wav';  % input audio filename
[pathstr,name,ext] = fileparts(wav_file);
% get parent directory 
parts = strsplit(pathstr, '\');
parent_dir = strjoin(parts(1:5), '\');

% implement for loop to analyse successive segments of the audio file
segment_size = 100000;
i=200000;

% Read speech samples, sampling rate and precision from file
[ speech, fs ] = audioread( char(wav_file) , [i i+segment_size]);

%sound(speech,fs);

fig = figure('Visible','off'); spectrogram(speech, 1024);
saveas(fig, strcat( parent_dir , '\spectrograms\', name, '.jpg'));




