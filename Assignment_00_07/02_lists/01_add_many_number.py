def sum_of_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def main():
    numbers_list = [10, 20, 30, 40, 50]
    result = sum_of_numbers(numbers_list)
    print("List:", numbers_list)
    print("Sum of numbers:", result)
    
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
