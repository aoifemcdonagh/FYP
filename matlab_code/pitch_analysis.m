% Script to analyse the pitch of speech samples of female speakers

close all
clc

samplesize=1000000;

samplepaths = {'U:\My Documents\4th Year\FYP\Irish Language\Ulaidh\Ronan-Bruscar-C1-Bliain1-2011.wav','U:\My Documents\4th Year\FYP\Irish Language\Connacht\C1 Connacht\17 Norita.wav','U:\My Documents\4th Year\FYP\Irish Language\Mumhan\C1 Bliain 1 Mumhan\14 Odí.wav'};

%iterate though the files chosen
for path1=samplepaths
    % Audio sample
    [x,Fs] = audioread(path1{1},[300000 samplesize]); 
    %sound(x,Fs);

    [f0_time,f0_value,SHR,f0_candidates] = shrp(x,Fs,[[120 400], 40, 10, 0.4, 1250, 0, 0]);

    figure; plot(f0_time, f0_value);
    xlabel('Times of F0 values'); ylabel('F0 Values'); 
    title('Plot of F0 for speech samples');
    
    %{
    figure; plot(SHR);
    xlabel(''); ylabel(''); 
    title('')

    figure; plot(f0_candidates);
    xlabel(''); ylabel(''); 
    title('')
    %}
    
    % Calculate the average pitch:
    disp(path1);
    disp(mean(f0_value));
end
