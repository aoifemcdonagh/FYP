% Aoife McDonagh
% 13411348
% Script for creating MFCC plots for use in CNN
% 
% Important Variables:
% 
%   start_pause:    an estimate for the length of time at the start of a 
%                   file before the speaker begins speaking. This does not
%                   need to be analysed.
%   
%   segment_size:   the size of each speech segment to be analysed. This
%                   should be just long enough for a listener to determine
%                   what accent is being spoken and no longer.
%
%   audio_file_location:    directory where the audio files to be analysed
%                           can be found.
%
%   MFCC_location:          directory where Matlab will save the
%                           spectrograms it creates during a test run.
%
%   test_MFCCs:             directory within 'MFCC_location' where
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

audio_file_location = 'U:\My Documents\4th Year\FYP\Irish Language\Files for analysis\Cleaned Files';
MFCC_location = strcat(audio_file_location, '\MFCCs');
test_MFCCs = fullfile(MFCC_location, date);

if exist(MFCC_location, 'dir') == 7 % Check if this dir exists
    mkdir(test_MFCCs);   % Create a folder to store MFCCs from this test run
else    % Create a folder to store MFCCs from test runs if it doesn't already exist.
   MFCC_location = mkdir(audio_file_location, '\MFCCs'); 
   mkdir(test_MFCCs);    % Create a folder to store MFCCs from this test run
end

files = dir(fullfile(audio_file_location, '*.wav'));    % 'files' contains any .wav files in this folder

for i=1:length(files) %Iterate through the files specified above
    [pathstr,name,ext] = fileparts(files(i).name); % Get name of file
    [ speech, fs ] = audioread( files(i).name );
    
    Tw = 25;     % analysis frame duration (ms)
    Ts = 10;                    % analysis frame shift (ms)
    alpha = 0.97;               % preemphasis coefficient
    R = [ 300 3700 ];           % frequency range to consider
    M = 20;                     % number of filterbank channels 
    C = 13;                     % number of cepstral coefficients
    L = 22;                     % cepstral sine lifter parameter
    
    for j=1:segment_size:(size(speech)-segment_size) % Iterate through until EOF
        % Read speech samples, sampling rate and precision from file
        
        speechj = speech(j:j+segment_size);
        
        fig = figure('Visible','off'); 
        [ MFCCs, FBEs, frames ] = mfcc(speechj, fs, Tw, Ts, alpha, @hamming, R, M, C+1, L);
        
         % Generate data needed for plotting 
        [ Nw, NF ] = size( frames );                % frame length and number of frames
        time_frames = [0:NF-1]*Ts*0.001+0.5*Nw/fs;  % time vector (s) for frames 
        time = [ 0:segment_size ]/fs;           % time vector (s) for signal samples 
        logFBEs = 20*log10( FBEs );                 % compute log FBEs for plotting
        logFBEs_floor = max(logFBEs(:))-50;         % get logFBE floor 50 dB below max
        logFBEs( logFBEs<logFBEs_floor ) = logFBEs_floor; % limit logFBE dynamic range


        % Generate plots
        figure('Position', [30 30 800 600], 'PaperPositionMode', 'auto', ... 
                  'color', 'w', 'PaperOrientation', 'landscape', 'Visible', 'off' ); 

        subplot( 311 );
        plot( time, speechj, 'k' );
        xlim( [ min(time_frames) max(time_frames) ] );
        xlabel( 'Time (s)' ); 
        ylabel( 'Amplitude' ); 
        title( 'Speech waveform'); 

        subplot( 312 );
        imagesc( time_frames, [1:M], logFBEs ); 
        axis( 'xy' );
        xlim( [ min(time_frames) max(time_frames) ] );
        xlabel( 'Time (s)' ); 
        ylabel( 'Channel index' ); 
        title( 'Log (mel) filterbank energies'); 

        subplot( 313 );
        %imagesc( time_frames, [1:C], MFCCs(2:end,:) ); % HTK's TARGETKIND: MFCC
        imagesc( time_frames, [1:C+1], MFCCs );       % HTK's TARGETKIND: MFCC_0
        axis( 'xy' );
        xlim( [ min(time_frames) max(time_frames) ] );
        xlabel( 'Time (s)' ); 
        ylabel( 'Cepstrum index' );
        title( 'Mel frequency cepstrum' );

        % Set color map to grayscale
        colormap( 1-colormap('gray') ); 

        % Print figure to pdf and png files
        print('-dpdf', sprintf('%s.pdf', mfilename)); 
        print('-dpng', sprintf('%s.png', mfilename)); 

        saveas(gcf, strcat(test_MFCCs, '\', name, '_' , num2str(j+segment_size), '.jpg'));

    end
end