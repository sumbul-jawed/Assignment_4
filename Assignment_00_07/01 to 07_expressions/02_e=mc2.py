def main():
    C = 299792458  # meters per second

    # Input from the user
    mass = float(input("Enter kilos of mass: "))

    # Calculate energy using E = m * c^2
    print("\ne = m * C^2...\n")
    print(f"m = {mass} kg")
    print(f"C = {C} m/s")

    energy = mass * C ** 2
    print(f"\n{energy} joules of energy!")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
