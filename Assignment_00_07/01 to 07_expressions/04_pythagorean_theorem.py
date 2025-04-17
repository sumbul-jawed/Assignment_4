import math

def main():
    # Get the two side lengths from the user and cast them to be numbers
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))

    # Calculate the hypotenuse using the two sides and print it out
    bc = math.sqrt(ab ** 2 + ac ** 2)

    # Result print karein
    print("The length of BC (the hypotenuse) is:", bc)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
