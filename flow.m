close all; clear all;
%==================================
% setup stuff
%==================================
%THESE SEEM USEFUL
%x1(0) = x10;
%x2(0) = x20;

%THESE ARE USEFUL
a = 0.831; % mortality rate of predator
b = 0.0162; % reproduction rate of predator per prey
c = 0.2824; % reproduction rate of prey
d = 0.0211; % mortality rate of predator per prey
x10 = 10; % initial predator population
x20 = 40; % initial prey population

%THESE ARE OUR ODEs
% x1p = -a*x1 + b*x1*x2;
% x2p = c*x2 - d*x1*x2;

%JACOBIAN MATRIX
%J = [-a+b*x2 b*x1; -d*x2 c-d*x1];



%==================================
% 2.3
%==================================
%1) nullclines and equ poins
    %x1p == 0;
        %x1 = 0;
        %x2 = a/b;
    %x2p == 0;
        %x2 = 0;
        %x1 = c/d;
    %equ pts
        %c/d = a/b;
        %x1 = x2 = 0;
        
%2) eigenvalues
    % lam = (-(a-c) +- sqrt((a-c)^2 +4))/2
    % lam = 0, 0.7627, -1.311;
    
%3) stability
    % 0.7627 unstable
    % -1.311 stable
    % 0 neutrally stable
    % a/b || c/d == one of these values 

%==================================
% 2.4
%==================================
% Set the axis limits
sz = 50;
x1min = -sz; 
x1max = sz; 
x2min = -sz; 
x2max = sz;
%set step size for x1 and x2;
x1step = 1; 
x2step = 1; 
%generate mesh for plotting
[x1, x2] = meshgrid(x1min:1:x2max, x2min:1:x2max);

% Define the system of equations 
dx1 = -a*x1 + b*x1*x2;
dx2 = c*x2 - d*x1*x2;

%normalize vectors (to help plotting)
dx1 = dx1./sqrt(dx1.^2 + dx2.^2); 
dx2 = dx2./sqrt(dx1.^2 + dx2.^2);

% Generate the vector field
figure;
quiver(x1, x2, dx1,dx2,'AutoScaleFactor',0.5); hold on;


%PUT IN A LINE FOR a/b AND c/d
x = linspace(-sz, sz);
y = linspace(-sz, sz);
plot(a/b, y);
plot(x, c/d); hold off;

%change axes limits, add labels
axis([x1min x1max x2min x2max])
xlabel('$x_1$','Interpreter','latex')
ylabel('$x_2$','Interpreter','latex')


