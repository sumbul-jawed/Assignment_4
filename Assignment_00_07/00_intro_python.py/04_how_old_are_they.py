def main():
    anton : int = 21  # Anton's age is given as 21 years old
    beth : int = 6 + anton  # Beth is 6 years older than Anton, so add 6 to Anton's age to get Beth's
    chen : int = 20 + beth  # Chen is 20 years older than Beth, so add 20 to Beth's age to get Chen's
    drew  : int= chen + anton  # Drew is as old as Chen's age plus Anton's age, so add them together
    ethan : int = chen  # Ethan is the same age as Chen, so set Ethan's age equal to Chen's

    print("Anton is", anton)
    print("Beth is", beth)
    print("Chen is", chen)
    print("Drew is", drew)
    print("Ethan is", ethan)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
