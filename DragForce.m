% by jake suddreth
% warning('off')
clc;
time = 0:0.00000435:0.435;
% acceleration due to gravity 
g = 32.174; % ft/s^2
A = (pi/4)*(33^2); %ft^2
C = 0.515; % coefficient of drag
f = @(t, n) [n(2); ((7.6*10^6)-(103.44*exp(-4*10^(-5)*n(2))*C*A*n(1)^2)-(g*(6.2*10^6)-4*t*10^4))/((6.2*10^6)-4*t*10^4)];
IC = [0, 1.4*10^3];
[t, n] = ode45(f, time, IC);
y = n(:,1);
y_file = fopen('y_values_df.txt', 'w');
fprintf(y_file, '%12.16f\n', y);
fclose(y_file);
d = (103.44*exp(-4*10^(-5).*n(:,2)).*C*A.*n(:,1).^2);
d_file = fopen('d_values_df.txt', 'w');
fclose(d_file);
