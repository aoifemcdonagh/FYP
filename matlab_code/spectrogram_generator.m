% Aoife McDonagh
% 13411348
% Script for creating spectograms for use in CNN
% 
% Important Variables:
% 
%   start_pause:    an estimate for the length of time at the start of a 
%                   file before the speaker begins speaking. This does not
%                   need to be analysed.
%                   Might not be necessary???
%   
%   segment_size:   the size of each speech segment to be analysed. This
%                   should be just long enough for a listener to determine
%                   what accent is being spoken and no longer.
%
%   audio_file_location:    directory where the audio files to be analysed
%                           can be found.
%
%   spectrogram_location:   directory where Matlab will save the
%                           spectrograms it creates during a test run.
%
%   test_spectrograms:      directory within 'spectrogram_location' where
%                           spectrograms for individual test runs are
%                           stored.
%
%   date:           Date and time string to use in folder naming need to 
%                   remove the colons as they cannot be used when naming a
%                   folder.

clc
clear all
close all

start_pause = 10000;
segment_size = 50000;
date = strrep(datestr(now), ':', ''); 
date = strrep(date, ' ', '_');  

audio_file_location = '/media/sf_tensorflow_VM/audio/cleaned_files';
spectrogram_location = strcat(audio_file_location, '\spectrograms');
test_spectrograms = fullfile(spectrogram_location, date);

if exist(spectrogram_location, 'dir') == 7 % Check if this dir exists
    [status, msg, msgid] = mkdir(test_spectrograms);   % Create a folder to store spectrograms from this test run
else    % Create a folder to store spectrograms from test runs if it doesn't already exist.
   [status1, msg1, msgid1] = mkdir(spectrogram_location); 
   [status2, msg2, msgid2] = mkdir(test_spectrograms);    % Create a folder to store spectrograms from this test run
end

files = dir(fullfile(audio_file_location, '*.wav'));    % 'files' contains any .wav files in this folder

for i=1:length(files) %Iterate through the files specified above
    [pathstr,name,ext] = fileparts(files(i).name); % Get name of file
    [ speech, fs ] = audioread( files(i).name );
    
    for j=1:segment_size:(size(speech)-segment_size) % Iterate through until EOF
        % Read speech samples, sampling rate and precision from file

        fig = figure('Visible','off'); spectrogram(speech(j:j+segment_size), 128);
        saveas(gcf, strcat(test_spectrograms, '\', name, '_' , num2str(j+segment_size), '.jpg'));
    end
end