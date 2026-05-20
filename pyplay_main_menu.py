# pyplay_main_menu.py
# This is the main menu file for the PyPlay system.

# Import the toolkit file so the menu can call the games
import pyplay_toolkit as toolkit

# Function to display the main menu
def show_menu():
    print("\n====================")
    print("      PyPlay")
    print("====================")
    print("1. Geography Quiz")
    print("2. Number Guessing Game")
    print("3. Even or Odd Checker")
    print("4. Exit")
    print("====================")

# Main program loop
def main():
    while True:
        # Show the menu every time the loop starts
        show_menu()

        try:
            # Cast user input to an integer for menu selection
            choice = int(input("Choose an option (1-4): "))
        except ValueError:
            # Handle invalid menu input
            print("Invalid input. Please enter a number from 1 to 4.")
            continue

        # Run the selected tool based on the user's choice
        if choice == 1:
            toolkit.geography_quiz()
        elif choice == 2:
            toolkit.number_guessing_game()
        elif choice == 3:
            toolkit.even_or_odd_checker()
        elif choice == 4:
            print("Thank you for using PyPlay. Goodbye!")
            break
        else:
            print("Please choose a valid option from 1 to 4.")

        # Pause before returning to the menu
        input("\nPress Enter to return to the main menu...")

# Start the program
if __name__ == "__main__":
    main()
