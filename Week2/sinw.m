clc;
clear all;
close all;
t = 0:0.01:1;
f = 2;
x = sin(2 * pi * f * t);
plot(t, x);
xlabel('Time');
ylabel('Amplitude');
title('Sine Wave with Frequency 2');

