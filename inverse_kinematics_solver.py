import sys
sys.path.append('..')
from GP25Plotter import robo_plot as rp
import numpy as np
import modern_robotics as mr

x_co = 0
y_co = 0
z_co = 0

S = np.array([[0, 0, 1, 0, 0, 0],
              [0, 1, 0, -0.505, 0, 0.150],
              [0, 1, 0, -1.265, 0, 0.150],
              [1, 0, 0, 0, 1.465, 0],
              [0, 1, 0, -1.465, 0, 0.945],
              [1, 0, 0, 0, 1465, 0]]).T


M = np.array([[1, 0, 0, 1.045],
              [0, 1, 0, 0],
              [0, 0, 1, 1.465],
              [0, 0, 0, 1]])

eomg = 0.01
ev = 0.001
thetalist0 = [0, 0, 0, 0, 0, 0]

T = np.array([[1, 0, 0, x_co],
              [0, 1, 0, y_co],
              [0, 0, 1, z_co],
              [0, 0, 0, 1]])

thetalist, sucess = mr.IKinSpace(S, M, T, thetalist0, eomg, ev)

np.set_printoptions(suppress=True, precision=3)

if sucess:
    rp.robo_plot(thetalist)
    print(thetalist)
else:
    print("No valid pose was found")