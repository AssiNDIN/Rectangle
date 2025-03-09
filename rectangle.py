def getValidInteger(prompt):
    """Function to get a valid integer input from the user"""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def drawRectangle(height, length):
    """Draws a rectangle using asterisks (*)"""
    print("\nRectangle representation:\n")
    for i in range(height):
        if i == 0 or i == height - 1:
            print("*" * length)  # Top and bottom borders
        else:
            print("*" + " " * (length - 2) + "*")  # Side borders with spaces

def main():
    """Main function to handle user input and looping"""
    while True:
        # Get valid height and length
        height = getValidInteger("Enter the height of the rectangle: ")
        length = getValidInteger("Enter the length of the rectangle: ")

        # Calculate area and perimeter
        area = height * length
        perimeter = 2 * (height + length)

        # Displaying results
        print(f"\nArea of the rectangle: {area}")
        print(f"Perimeter of the rectangle: {perimeter}")

        # Call function to draw rectangle
        drawRectangle(height, length)

        # Ask user if they want to continue
        while True:
            choice = input("\nDo you want to continue? (y/n): ").strip().lower()
            if choice == 'y':
                break  # Continue the loop
            elif choice == 'n':
                print("Goodbye!")
                return  # Exit the program
            else:
                print("Command not found. Please enter 'y' or 'n'.")


if __name__ == "__main__":
    main()
