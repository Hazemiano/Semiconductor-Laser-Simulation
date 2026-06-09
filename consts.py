import numpy as np

X = 4
Y = 4
L = (200+30*X)*1e-4
R = 0.3+0.02*Y
W = 2e-4
D = 0.2e-4
GAMMA = 0.3
NG = 4
ALPHA_INT = 40
B = 2.5e-16
N0 = 1e18 # transparency carrier density
TAU = 2.2e-9 # spontaneous lifetime
BETA_SP = 1e-4 # spontaenous emission factor
H = 6.62607015e-34
C = 3e10

vg = C/NG # group velocity
ALPHA_M=(1/(2*L))*(np.log((1/(R*R))))
alpha_tot = ALPHA_INT + ALPHA_M # total alpha loss
V = L * D * W # volume of the diode
tau_ph = 1/(vg*alpha_tot) # photon lifetime 
g_th = alpha_tot / GAMMA; # gain 
q = 1.6*1e-19 # electric charge
lamda = 1.55e-4 # operating wavelength (assumed to be 1.55um)
freq = C/lamda

Nth = 1/(GAMMA * B * vg * tau_ph) + 1e18  # carrier density at threshold
Jth = Nth * q * D / TAU  # current density at threshold
Ith = Jth * L * W  # threshold current