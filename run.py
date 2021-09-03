def main_menu():
    """
    Function to display the main menu options and capture user selection
    """
    print("\nWelcome to Chris' Conversion Compendium")
    print("")
    print("MAIN MENU")
    print("")
    print("Enter the number of the conversion type below")
    print("-" * 69)
    print("1. Temperature")
    print("2. Length")
    print("3. Volume")
    print("4. Currency")

    selection = input("\nPlease enter your selection here:")

    if selection == ("1"):
        Temperature.convert_temp()
    elif selection == ("2"):
        convert_length()
    elif selection == ("3"):
        convert_volume()
    elif selection == ("4"):
        convert_currrency()


class Temperature:
    def convert_temp():
        """
        Function to convert temperatures. Function first checks if selection
        is what the user intended. If not it loops back to main menu.
        """
        print("\nYou have selected Temperature. Is this correct?")

        confirm_type = input("\nY/N:").upper()

        if confirm_type == ("Y"):
            print("\nSelect starting unit in Celsius, Farenheit or Kelvin")
            temp_selection = input("Unit Type (C,F or K):").upper()
            temp_value = float(input("\nPlease enter the temperature to convert:"))

        elif confirm_type == ("N"):
            main_menu()


def convert_length():
    print("worked2")


def convert_volume():
    print("worked3")


def convert_currrency():
    print("worked4")


main_menu()
