def main_menu():
    """
    Function to display the main menu options and capture user selection
    """
    print("Welcome to Chris' Conversion Compendium")
    print("")
    print("MAIN MENU")
    print("")
    print("Enter the number of the conversion type below")
    print("-" * 69)
    print("1. Temperature")
    print("2. Length")
    print("3. Volume")
    print("4. Currency")

    selection = input("Please enter your selection here:")

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
        print("You have selected Temperature. Is this correct?")

        confirm_type = input("Y/N:")

        if confirm_type == ("Y"):
            print("Please select your starting unit. Enter C, F or K to start with Celsius, Farenheit or Kelvin")
            temp_unit = input("Unit Type (C,F or K):")
        else: 
            main_menu()




def convert_length():
    print("worked2")


def convert_volume():
    print("worked3")


def convert_currrency():
    print("worked4")


main_menu()
