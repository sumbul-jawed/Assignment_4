def main():
    feet = float(input("Enter the number of feet: "))
    # Convert feet to inches
    inches = feet * 12

    print(f"{feet} feet is equal to {inches} inches.")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
