%close all
clc

max=100000;

[x,Fs] = audioread('U:\My Documents\4th Year\FYP\Matlab code\Odi.wav',[1 max]);

y=fft(x,max);
range=1:max;
figure; plot(range, y);

sound(x,Fs);
