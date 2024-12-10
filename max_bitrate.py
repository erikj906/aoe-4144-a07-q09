# max_bitrate.py
#
# Usage: python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz
# Implement the calculation for maximum achievable bitrate.
# Parameters:
#  tx_w: Transmitted power in watts
#  tx_gain_db: Transmitter gain in dB
#  freq_hz: Transmission frequency in Hz
#  dist_km: Separation vector magnitude between transmitter and receiver in km
#  rx_gain_db: Receiver gain in dB
#  n0_j: Noise spectral density in W/Hz
#  bw_hz: Channel bandwidth in Hz
# Output:
#  Print r_max (maximum achievable bitrate)
#
# Written by Erik Judy
# Other contributors: None
#
# See the LICENSE file for the license.

# import Python modules
import math # math module
import sys # argv

# "constants"
c = 2.99792458e8; # speed of light (m/s)

# initialize script arguments
tx_w = float('nan')
tx_gain_db = float('nan')
freq_hz = float('nan')
dist_km = float('nan')
rx_gain_db = float('nan')
n0_j = float('nan')
bw_hz = float('nan')

# parse script arguments
if len(sys.argv) == 8:
     tx_w = float(sys.argv[1])
     tx_gain_db = float(sys.argv[2])
     freq_hz = float(sys.argv[3])
     dist_km = float(sys.argv[4])
     rx_gain_db = float(sys.argv[5])
     n0_j = float(sys.argv[6])
     bw_hz = float(sys.argv[7])

else:
   print(\
    'Usage: '\
    'python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz'\
   )
   exit()

# write script below this line

lam = c/freq_hz 

L_A_dB = 0; 
L_A = 10**(L_A_dB/10); 
L_L_dB = -1; 
L_L = 10**(L_L_dB/10); 

G_t = 10**(tx_gain_db/10)
G_r = 10**(rx_gain_db/10)

C = tx_w*L_L*G_t*(lam/(4*math.pi*(dist_km*1000)))**2*L_A*G_r

N = n0_j*bw_hz
r_max = bw_hz*math.log2(1 + C/N)

print(math.floor(r_max)) 