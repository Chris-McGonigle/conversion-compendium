def main_menu():
    """
    Function to display the main menu options
    """
    print("Welcome to Chris' Conversion Compendium")
    print("")
    print("MAIN MENU")
    print("")
    print("Please enter the number of the conversion you would like to carry out")
    print("-" * 69)
    print("1. Temperature")
    print("2. Length")
    print("3. Volume")
    print("4. Currency")

    selection = input("Please enter your selection here:")

    if selection == ("1"):
        convert_temp()
    elif selection == ("2"):
        convert_length()
    elif selection == ("3"):
        convert_volume()
    elif selection == ("4"):
        convert_currrency()

def convert_temp():
    print("worked")

main_menu()

