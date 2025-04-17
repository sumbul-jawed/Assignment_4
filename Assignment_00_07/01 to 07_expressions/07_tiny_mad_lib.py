def main():
    # Get the three inputs from the user to make the adlib
    adjective = input("Please type an adjective and press enter: ")
    noun = input("Please type a noun and press enter: ")
    verb = input("Please type a verb and press enter: ")
    
    # Print the resulting sentence using the user inputs
    print(f"Code in Place is fun. I learned to program and used Python to make my {adjective} {noun} {verb}!")

# This provided line is required at the end of Python file to call the main() function.
if __name__ == '__main__':
    main()
