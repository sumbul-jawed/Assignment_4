def main():
    DAYS_IN_YEAR = 365
    HOURS_IN_DAY = 24
    MINUTES_IN_HOUR = 60
    SECONDS_IN_MINUTE = 60
    
    # We can get the number of seconds per year by multiplying the handy constants above!
    seconds_in_year = DAYS_IN_YEAR * HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE
    
    # Print the result
    print(f"There are {seconds_in_year} seconds in a year!")

# This provided line is required at the end of Python file to call the main() function.
if __name__ == '__main__':
    main()
