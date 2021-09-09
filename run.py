import pyinputplus as pyip
from forex_python.converter import CurrencyRates


def main_menu():
    """
    Function to display the main menu options and capture user selection
    """
    print("\nWelcome to Chris's Conversion Compendium")
    print("")
    print("MAIN MENU")
    print("")
    print("Enter the number of the conversion type below")
    print("-" * 45)
    print("1. Temperature")
    print("2. Length")
    print("3. Volume")
    print("4. Currency")

    selection = pyip.inputNum("\nPlease enter your selection here:",
                              lessThan=5)

    if selection == (1):
        Temperature.convert_temp()
    elif selection == (2):
        Length.convert_length()
    elif selection == (3):
        Volume.convert_volume()
    elif selection == (4):
        Currency.convert_currency()


class Temperature:
    def convert_temp():
        """
        Function to convert temperatures. Function first checks if selection
        is what the user intended. If not it loops back to main menu.
        It then takes the user input which is then passed through
        the calculation function
        """
        print("\nYou have selected Temperature. Is this correct?")

        confirm_type = pyip.inputYesNo("\nY/N:")

        if confirm_type == ("yes"):
            print("\nEnter the number of your starting unit.\n")
            temp_selection = pyip.inputMenu(["Celsius", "Fahrenheit", "Kelvin"
                                             ], numbered=True)
            temp_value = pyip.inputNum("\nPlease enter the temperature to convert:")
            if temp_selection == ("Celsius"):
                print(f"\n{temp_value} {temp_selection} converted equals:")
                print(f"\n{Temperature.celsius2fahrenheit(temp_value)} Fahrenheit")
                print(f"\n{Temperature.celsius2kelvin(temp_value)} Kelvin")
                Temperature.run_again()
            elif temp_selection == ("Fahrenheit"):
                print(f"\n{temp_value} {temp_selection} converted equals:")
                print(f"\n{Temperature.fahrenheit2celsius(temp_value)} Celsius")
                print(f"\n{Temperature.fahrenheit2kelvin(temp_value)} Kelvin")
                Temperature.run_again()
            elif temp_selection == ("Kelvin"):
                print(f"\n{temp_value} {temp_selection} converted equals:")
                print(f"\n{Temperature.kelvin2celsius(temp_value)} Celsius")
                print(f"\n{Temperature.kelvin2fahrenheit(temp_value)} Fahrenheit")
                Temperature.run_again()
        elif confirm_type == ("no"):
            main_menu()

    def celsius2kelvin(temp_value):
        """
        Conversion formula for Celsius to Kelvin
        """
        c2k = temp_value + 273.15
        return float("{:.2f}".format(c2k))

    def celsius2fahrenheit(temp_value):
        """
        Conversion formula for Celsius to Fahrenheit
        """
        c2f = (temp_value * 9/5) + 32
        return float("{:.2f}".format(c2f))

    def fahrenheit2celsius(temp_value):
        """
        Conversion formula for Fahrenheit to Celsius
        """
        f2c = (temp_value - 32) * 5/9
        return float("{:.2f}".format(f2c))

    def fahrenheit2kelvin(temp_value):
        """
        Conversion formula for Fahrenheit to Kelvin
        """
        f2k = (temp_value + 459.67) / 1.8
        return float("{:.2f}".format(f2k))

    def kelvin2celsius(temp_value):
        """
        Conversion formula for Kelvin to Celsius
        """
        k2c = temp_value - 273.15
        return float("{:.2f}".format(k2c))

    def kelvin2fahrenheit(temp_value):
        """
        Conversion formula for Kelvin to Fahrenheit
        """
        k2f = (temp_value * 1.8) - 459.67
        return float("{:.2f}".format(k2f))

    def run_again():
        """
        Refactored function that asks user do they want to convert again
        """
        print("-" * 45)
        print("\nWould you like to convert another Temperature?")
        convert_again = pyip.inputYesNo("\nY/N:")
        if convert_again == ("yes"):
            Temperature.convert_temp()
        else:
            main_menu()


class Length:
    def convert_length():
        """
        Function to convert length. Function first checks if selection
        is what the user intended. If not it loops back to main menu.
        It then takes the user input which is then passed through
        the calculation function
        """
        print("\nYou have selected Length. Is this correct?")

        confirm_type = pyip.inputYesNo("\nY/N:")

        if confirm_type == ("yes"):
            print("\nEnter the number of your starting unit\n")
            len_selection = pyip.inputMenu(["Nanometres", "Micrometres",
                                            "Millimetres", "Centimetres",
                                            "Metres", "Kilometres", "Inches",
                                            "Feet", "Yards", "Miles",
                                            "Nautical Miles"], numbered=True)
            len_value = pyip.inputNum("\nPlease enter the length to convert:")

            length_conversion_factors = {
                'Kilometres': {'Metres': 0.001,
                               'Centimetres': 0.00001,
                               'Millimetres': 0.000001,
                               'Micrometres': 0.000000001,
                               'Nanometres': 0.000000000001,
                               'Miles': 1.60934,
                               'Yards': 0.000914397727272727,
                               'Feet': 0.000304799242424242,
                               'Inches': 2.54e-5,
                               'Nautical Miles': 1.852},

                'Metres': {'Kilometres': 1000,
                           'Centimetres': 0.01,
                           'Millimetres': 0.001,
                           'Micrometres': 0.000001,
                           'Nanometres': 0.000000001,
                           'Miles': 1609.34,
                           'Yards': 0.914397727272727,
                           'Feet': 0.304799242424242,
                           'Inches': 0.0253999368686869,
                           'Nautical Miles': 1852},

                'Centimetres': {'Kilometres': 100000,
                                'Metres': 100,
                                'Millimetres': 0.1,
                                'Micrometres': 0.0001,
                                'Nanometres': 0.0000001,
                                'Miles': 160934,
                                'Yards': 91.4397727272727,
                                'Feet': 30.4799242424242,
                                'Inches': 2.53999368686869,
                                'Nautical Miles': 185200},

                'Millimetres': {'Kilometres': 1000000,
                                'Metres': 1000,
                                'Centimetres': 10,
                                'Micrometres': 0.001,
                                'Nanometres': 0.000001,
                                'Miles': 1609340,
                                'Yards': 914.397727272727,
                                'Feet': 304.799242424242,
                                'Inches': 25.3999368686869,
                                'Nautical Miles': 1852000},

                'Micrometres': {'Kilometres': 1000000000,
                                'Metres': 1000000,
                                'Centimetres': 10000,
                                'Millimetres': 1000,
                                'Nanometres': 0.001,
                                'Miles': 1609340000,
                                'Yards': 914397.727272727,
                                'Feet': 304799.242424242,
                                'Inches': 25399.9368686869,
                                'Nautical Miles': 1852000000},

                'Nanometres': {'Kilometres': 1000000000000,
                               'Metres': 1000000000,
                               'Centimetres': 10000000,
                               'Millimetres': 1000000,
                               'Micrometres': 1000,
                               'Miles': 1609340000000,
                               'Yards': 914397727.272727,
                               'Feet': 304799242.424242,
                               'Inches': 25399936.8686869,
                               'Nautical Miles': 1852000000000},

                'Miles': {'Kilometres': 0.621371,
                          'Metres': 0.000621371,
                          'Centimetres': 0.00000621371,
                          'Millimetres': 0.000000621371,
                          'Micrometres': 0.000000000621371,
                          'Nanometres': 0.000000000000621371,
                          'Yards': 0.000568180230193182,
                          'Feet': 0.000189393410064394,
                          'Inches': 1.57827841720328E-05,
                          'Nautical Miles': 1.150779092},

                'Yards': {'Kilometres': 1093.61296,
                          'Metres': 1.09361296,
                          'Centimetres': 0.0109361296,
                          'Millimetres': 0.00109361296,
                          'Micrometres': 0.00000109361296,
                          'Nanometres': 0.00000000109361296,
                          'Miles': 1760,
                          'Feet': 0.333332401713333,
                          'Inches': 0.0277777001427778,
                          'Nautical Miles': 2025.37120192},

                'Feet': {'Kilometres': 3280.83888,
                          'Metres': 3.28083888,
                          'Centimetres': 0.0328083888,
                          'Millimetres': 0.00328083888,
                          'Micrometres': 0.00000328083888,
                          'Nanometres': 0.00000000328083888,
                          'Miles': 5280,
                          'Yards': 3,
                          'Inches': 0.0833331004283333,
                          'Nautical Miles': 6076.11360576},

                'Inches': {'Kilometres': 39370.06656,
                           'Metres': 39.37006656,
                           'Centimetres': 0.3937006656,
                           'Millimetres': 0.03937006656,
                           'Micrometres': 0.00003937006656,
                           'Nanometres': 0.00000003937006656,
                           'Miles': 63360,
                           'Yards': 36,
                           'Feet': 12,
                           'Nautical Miles': 72913.36326912},

                'Nautical Miles': {'Kilometres': 0.539957,
                                   'Metres': 0.000539957,
                                   'Centimetres': 0.00000539957,
                                   'Millimetres': 0.000000539957,
                                   'Micrometres': 0.000000000539957,
                                   'Nanometres': 0.000000000000539957,
                                   'Miles': 0.86897439838,
                                   'Yards': 0.000493735453625,
                                   'Feet': 0.000164578484541667,
                                   'Inches': 1.37148737118056E-05},
            }

            print(f"\n{len_value} {len_selection} converted equals:")

            if len_selection in length_conversion_factors:
                for value in length_conversion_factors[len_selection]:
                    conv_value = round(len_value / float(
                                        length_conversion_factors
                                        [len_selection][value]), 4)
                    print(f"\n{conv_value} {value}")
            Length.run_again()

        elif confirm_type == ("no"):
            main_menu()

    def run_again():
        """
        Function that asks user do they want to convert again
        """
        print("-" * 45)
        print("\nWould you like to convert another Length?")
        convert_again = pyip.inputYesNo("\nY/N:")
        if convert_again == ("yes"):
            Length.convert_length()
        else:
            main_menu()


class Volume:
    def convert_volume():
        """
        Function to convert volume. Function first checks if selection
        is what the user intended. If not it loops back to main menu.
        It then takes the user input which is then passed through
        the calculation function
        """
        print("\nYou have selected Volume. Is this correct?")

        confirm_type = pyip.inputYesNo("\nY/N:")

        if confirm_type == ("yes"):
            print("\nEnter the number of your starting unit\n")
            vol_selection = pyip.inputMenu(["Millilitre",
                                            "Litre",
                                            "Cubic Metre",
                                            "Cubic Foot",
                                            "Cubic Inch",
                                            "Imperial Cup",
                                            "Imperial Pint",
                                            "Imperial Gallon",
                                            "US Cup",
                                            "US Pint",
                                            "US Gallon", ], numbered=True)
            vol_value = pyip.inputNum("\nPlease enter the volume to convert:")

            volume_conversion_factors = {
                'millilitre': {'litre': 1000,
                               'cubic meter': 1000000,
                               'cubic foot': 28316.8,
                               'cubic inch': 16.3871,
                               'imperial cup': 284.131,
                               'imperial pint': 568.261,
                               'imperial gallon': 4546.09,
                               'us cup': 240,
                               'us pint': 473.176,
                               'us gallon': 3785.41},

                'litre': {'millilitre': 0.001,
                          'cubic meter': 1000,
                          'cubic foot': 28.3168,
                          'cubic inch': 0.0163870370367249,
                          'imperial cup': 0.284131,
                          'imperial pint': 0.568261,
                          'imperial gallon': 4.54609,
                          'us cup': 0.24,
                          'us pint': 0.473176,
                          'us gallon': 3.78541},

                'cubic metre': {'millilitre': 0.000001,
                                'litre': 0.001,
                                'cubic foot': 0.0283168,
                                'cubic inch': 0.000016387064,
                                'imperial cup': 0.000284131,
                                'imperial pint': 0.000568261,
                                'imperial gallon': 0.00454609,
                                'us cup': 0.00024,
                                'us pint': 0.000473176,
                                'us gallon': 0.00378541},

                'cubic foot': {'millilitre': 0.000035314666721489,
                               'litre': 0.0353147,
                               'cubic metre': 35.3147,
                               'cubic inch': 0.000578704,
                               'imperial cup': 0.010034,
                               'imperial pint': 0.020068,
                               'imperial gallon': 0.160544,
                               'us cup': 0.00847552,
                               'us pint': 0.0167101,
                               'us gallon': 0.133681},

                'cubic inch': {'millilitre': 0.0610237,
                               'litre': 61.0237,
                               'cubic metre': 61023.7,
                               'cubic foot': 1728,
                               'imperial cup': 17.3387,
                               'imperial pint': 34.6774,
                               'imperial gallon': 277.419,
                               'us cup': 14.6457,
                               'us pint': 28.875,
                               'us gallon': 231},

                'imperial cup': {'millilitre': 0.00351951,
                                 'litre': 3.51951,
                                 'cubic metre': 3519.51,
                                 'cubic foot': 99.6614,
                                 'cubic inch': 0.0576744,
                                 'imperial pint': 2,
                                 'imperial gallon': 16,
                                 'us cup': 0.844682,
                                 'us pint': 1.66535,
                                 'us gallon': 13.3228},

                'imperial pint': {'millilitre': 0.00175975,
                                  'litre': 1.75975,
                                  'cubic metre': 1759.75,
                                  'cubic foot': 49.8307,
                                  'cubic inch': 0.0288372,
                                  'imperial cup': 0.5,
                                  'imperial gallon': 8,
                                  'us cup': 0.422341,
                                  'us pint': 0.832674,
                                  'us gallon': 6.66139},

                'imperial gallon': {'millilitre': 0.000219969,
                                    'litre': 0.219969,
                                    'cubic metre': 219.969,
                                    'cubic foot': 6.22884,
                                    'cubic inch': 0.00360465,
                                    'imperial cup': 0.0625,
                                    'imperial pint': 0.125,
                                    'us cup': 0.0527926,
                                    'us pint': 0.104084,
                                    'us gallon': 0.832674},

                'us cup': {'millilitre': 0.00416667,
                           'litre': 4.16667,
                           'cubic metre': 4166.67,
                           'cubic foot': 117.986955189,
                           'cubic inch': 0.0682794,
                           'imperial cup': 1.18388,
                           'imperial pint': 2.36776,
                           'imperial gallon': 18.942,
                           'us pint': 1.97157,
                           'us gallon': 15.7725},

                'us pint': {'millilitre': 0.00211338,
                            'litre': 2.11338,
                            'cubic metre': 2113.38,
                            'cubic foot': 59.8442,
                            'cubic inch': 0.034632,
                            'imperial cup': 0.600475,
                            'imperial pint': 1.20095,
                            'imperial gallon': 9.6076,
                            'us cup': 0.50721,
                            'us gallon': 8},

                'us gallon': {'millilitre': 0.000264172,
                              'litre': 0.264172,
                              'cubic metre': 264.172,
                              'cubic foot': 7.48052,
                              'cubic inch': 0.004329,
                              'imperial cup': 0.0750594,
                              'imperial pint': 0.150119,
                              'imperial gallon': 1.20095,
                              'us cup': 0.0634013,
                              'us pint': 0.125},
            }
            volume_key = vol_selection.lower()

            print(f"\n{vol_value} {vol_selection}s converted equals:")

            if volume_key in volume_conversion_factors:
                for value in volume_conversion_factors[volume_key]:
                    conv_value = round(vol_value / float(
                                        volume_conversion_factors
                                        [volume_key][value]), 4)
                    print(f"\n{conv_value} {value}s")
            Volume.run_again()

        elif confirm_type == ("no"):
            main_menu()

    def run_again():
        """
        Function that asks user do they want to convert again
        """
        print("-" * 45)
        print("\nWould you like to convert another Volume?")
        convert_again = pyip.inputYesNo("\nY/N:")
        if convert_again == ("yes"):
            Volume.convert_volume()
        else:
            main_menu()


class Currency:
    def convert_currency():
        """
        Function to convert currency. Function first checks if selection
        is what the user intended. If not it loops back to main menu.
        It then takes the user input which is then passed through
        the calculation function. This function operates with real time
        values via the thrid party module forex-python
        """

        print("\nYou have selected Currency. Is this correct?")

        confirm_type = pyip.inputYesNo("\nY/N:")

        if confirm_type == ("yes"):
            print("\nEnter the number of your starting currency.\n")
            cur_selection = pyip.inputMenu(["AUD",
                                            "CAD",
                                            "CHF",
                                            "CNY",
                                            "EUR",
                                            "GBP",
                                            "INR",
                                            "JPY",
                                            "NZD",
                                            "RUB",
                                            "USD"], numbered=True)
            
            cur_value = pyip.inputNum("\nPlease enter the amount of currency to convert:")

            print("\nEnter the number of the currency to convert to:\n")
            
            cur_output = pyip.inputMenu(["AUD",
                                         "CAD",
                                         "CHF",
                                         "CNY",
                                         "EUR",
                                         "GBP",
                                         "INR",
                                         "JPY",
                                         "NZD",
                                         "RUB",
                                         "USD"], numbered=True)

            c = CurrencyRates()
            cur_result = c.convert(cur_selection, cur_output, cur_value)
            final_result = round(cur_result, 2)

            print(f"\n {cur_value} {cur_selection} converts to {final_result} {cur_output}")
            Currency.run_again()

   
        elif confirm_type == ("no"):
            main_menu()

    def run_again():
        """
        Function that asks user do they want to convert again
        """
        print("-" * 45)
        print("\nWould you like to convert another Currency?")
        convert_again = pyip.inputYesNo("\nY/N:")
        if convert_again == ("yes"):
            Currency.convert_currency()
        else:
            main_menu()

main_menu()
