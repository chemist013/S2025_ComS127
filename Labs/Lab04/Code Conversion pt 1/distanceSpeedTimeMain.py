# Joshua Hamaker        02/15/2025
# Lab 04 - Distance from Speed & Time w/ def main()

def main():
    print(f"This program calculates the distance an object traveled")
    speed = float(input(f"Enter the speed of the object in m/s: "))
    time = float(input(f"Enter the time the object traveled {speed} m/s in seconds: "))
    ans = distanceSpeedTime(speed, time)
    print(f"The distance the object traveled is {ans} metres!")

def distanceSpeedTime(v,t):
    deltaX = v*t
    return deltaX

if __name__ == "__main__":
    main()