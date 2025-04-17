def main():
    # Get the numbers we want to divide
    num1 = int(input("Please enter an integer to be divided: "))
    num2 = int(input("Please enter an integer to divide by: "))
    
    
    quotient = num1 // num2 # Divide with no remainder/decimals (integer division)
    remainder = num1 % num2 # Get the remainder of the division (modulus)


    # Output print karein
    print("The result of this division is", quotient, "with a remainder of", remainder)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
