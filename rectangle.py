"""
Lab Title: Rectangle 
Student Name: N'din Assi
course: CIS 216 OBJECT ORIENTED PROGRAMIMING 

"""

class Rectangle:
    """A class to represent a rectangle with methods to calculate area, perimeter, and draw it."""

    def __init__(self):
        """Initialize height and length after getting valid inputs."""
        self.height = self.get_valid_integer("Enter the height of the rectangle: ")
        self.length = self.get_valid_integer("Enter the length of the rectangle: ")

    def get_valid_integer(self, prompt):
        """Gets a valid integer input from the user."""
        while True:
            try:
                value = int(input(prompt))
                return value
            except ValueError:
                print("Invalid input! Please enter a valid integer.")

    def calculate_area(self):
        """Calculates and returns the area of the rectangle."""
        return self.height * self.length

    def calculate_perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        return 2 * (self.height + self.length)

    def draw_rectangle(self):
        """Draws the rectangle using asterisks (*)"""
        print("\nRectangle representation:\n")
        for i in range(self.height):
            if i == 0 or i == self.height - 1:
                print("*" * self.length)  # Top and bottom borders
            else:
                print("*" + " " * (self.length - 2) + "*")  # Side borders with spaces

    def display_info(self):
        """Displays the area, perimeter, and rectangle drawing."""
        print(f"\nArea of the rectangle: {self.calculate_area()}")
        print(f"Perimeter of the rectangle: {self.calculate_perimeter()}")
        self.draw_rectangle()


def main():
    """Main function to handle user interaction."""
    while True:
        # Create a rectangle object
        rect = Rectangle()
        
        # Display rectangle info
        rect.display_info()

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


# Run the program
if __name__ == "__main__":
    main()
