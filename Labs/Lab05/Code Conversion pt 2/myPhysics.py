# Joshua Hamaker      02/21/2025
# Lab05 - Physics Functions

# This is a module that contains the functions distanceSpeedTime() and
# velocity AccelerationTime() from Lab 04. These are to be called by calculationTest.py

def distanceSpeedTime(v: float, t: float) -> float:
    deltaX = v*t
    return deltaX

def velocityAccelerationTime(vi: float, a: float, t: float) -> float:
    vf = vi + a*t
    return vf