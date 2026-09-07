print("Welcome to the Pattern Generator")
print("and Number Analyzer!")

while True:
    print("\nSelect an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        rows = int(input("Enter the number of rows for the pattern: "))

        if rows <= 0:
            print("Invalid row count.")
            break

        print("\nPattern:")

        for i in range(1, rows + 1):
            for j in range(i):
                print("*", end="")
            print()

    elif choice == 2:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))

        if end < start:
            print("Invalid range.")
            continue

        total = 0

        for num in range(start, end + 1):

            if num % 2 == 0:
                print("Number", num, "is Even")
            else:
                print("Number", num, "is Odd")

            total = total + num

        print("Sum of all numbers from", start, "to", end, "is:", total)

    elif choice == 3:
        print("Exiting the program. Goodbye!")
        break

    else:
        pass
