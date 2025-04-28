# Joshua Hamaker        02/15/2025
# Lab 04 - Velocity from Acceleration & Time w/ def main()

def main():
    print(f"This program calculates the final velocity of an object")
    v_initial = float(input(f"Enter the initial velocity of the object in m/s: "))
    acc = float(input(f"Enter the object's acceleration in m/s/s: "))
    time = float(input(f"Enter the time the object traveled in seconds: "))
    ans = velocityAccelerationTime(v_initial, acc, time)
    print(f"The final velocity of  the object is {ans} m/s!")

def velocityAccelerationTime(vi,a,t):
    vf = vi + a*t
    return vf

if __name__ == "__main__":
    main()