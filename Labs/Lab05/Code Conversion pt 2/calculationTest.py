# Joshua Hamaker      02/21/2025
# Lab05 -

# This is a module that contains the main() function that calls functions from the modules
# myFinances.py, myOhmsLaw.py, myPhysics.py, and myShapes.py to be called by the user

import myFinances
import myOhmsLaw
import myPhysics
import myShapes

def main() -> None:
    quitProgram: bool = False
    while not quitProgram:
        print(f"1)  APR")
        print(f"2)  Compound Amount")
        print(f"3)  Distance")
        print(f"4)  Velocity")
        print(f"5)  Current")
        print(f"6)  Resistance")
        print(f"7)  Voltage")
        print(f"8)  Area of Rectangle")
        print(f"9)  Rectangle Perimeter")
        print(f"10) Area of Circle")
        print(f"11) Circle Circumference")
        print(f"[q]uit")
        calculation: str = input("Which calculation you would like to perform? ")
        match calculation:
            case "1":  # APR
                loanAmount: float = float(input(f"How much is the loan? "))
                daysInTerm: float = float(input(f"What is the length of th loan in days? "))
                interestCharges: float = float(input(f"How much interest will you be paying? "))
                fees: float = float(input(f"How much are the fees associated with the loan? "))
                ans1: float = myFinances.annualPercentageRate(interestCharges, fees, loanAmount, daysInTerm)
                print(f"Your loan's APR is {ans1}%!")
            case "2":  # Compound Amount
                principal: float = float(input(f"What is the principal of the loan? " ))
                rate: float = float(input(f"What is the interest rate of your account? (don't include '%') "))
                numberCompounds: float = float(input(f"How many times does your interest compound yearly? "))
                time2: float = float(input(f"How many years are you waiting? "))
                ans2: float = myFinances.compoundAmount(principal, rate, numberCompounds, time2)
                print(f"After {time2} years, you will have ${ans2} in your bank account!")
            case "3":  # Distance
                speed: float = float(input(f"Enter the speed of the object in m/s: "))
                time3: float = float(input(f"Enter the time the object traveled {speed} m/s in seconds: "))
                ans3: float = myPhysics.distanceSpeedTime(speed, time3)
                print(f"The distance the object traveled is {ans3} metres!")
            case "4":  # Velocity
                vInitial: float = float(input(f"Enter the initial velocity of the object in m/s: "))
                acc: float = float(input(f"Enter the object's acceleration in m/s/s: "))
                time4: float = float(input(f"Enter the time the object traveled in seconds: "))
                ans4 = myPhysics.velocityAccelerationTime(vInitial, acc, time4)
                print(f"The final velocity of  the object is {ans4} m/s!")
            case "5":  # Current
                voltage5: float = float(input(f"What is the voltage of the wire in volts? "))
                resistance5: float = float(input(f"What is the resistance of the wire in ohms? "))
                ans5: float = myOhmsLaw.calculateCurrent(voltage5, resistance5)
                print(f"The current of the wire is {ans5} amperes")
            case "6":  # Resistance
                current6: float = float(input(f"What is the current of the wire in amperes? "))
                voltage6: float = float(input(f"What is the voltage of the wire in volts? "))
                ans6: float = myOhmsLaw.calculateResistance(voltage6, current6)
                print(f"The resistance of the wire is {ans6} ohms")
            case "7":  # Voltage
                current7: float = float(input(f"What is the current of the wire in amperes? "))
                resistance7: float = float(input(f"What is the resistance of the wire in ohms? "))
                ans7: float = myOhmsLaw.calculateVoltage(current7, resistance7)
                print(f"The voltage of the wire is {ans7} volts")
            case "8":  # Area of Rectangle
                base8: float = float(input(f"What should the base of the rectangle be? "))
                height8: float = float(input(f"What should the height of the rectangle be? "))
                ans8: float = myShapes.areaOfRectangle(base8, height8)
                print(f"The area of your rectangle is {ans8}!")
            case "9":  # Rectangle Perimeter
                base9: float = float(input(f"What should the base of the rectangle be? "))
                height9: float = float(input(f"What should the height of the rectangle be? "))
                ans9: float = myShapes.rectanglePerimeter(base9, height9)
                print(f"The perimeter of your rectangle is {ans9}!")
            case "10": # Area of Circle
                radius10: float = float(input(f"What should the radius of the circle be? "))
                ans10: float = myShapes.areaOfCircle(radius10)
                print(f"The area of your circle is {ans10}!")
            case "11": # Circle Circumference
                radius11: float = float(input(f"What should the radius of the circle be? "))
                ans11: float = myShapes.circleCircumference(radius11)
                print(f"The circumference of your circle is {ans11}!")
            case "q":  # Quit
                quitProgram = True
            case _:
                print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()