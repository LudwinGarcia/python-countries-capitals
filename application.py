# -*- coding: utf-8 -*

"""
In this code you can find a possible good solution of
python-countries-capitals, these project freedom
analyze and restructure, if you find a better way
applying an area in the code, you can comment it on Github Issues
"""

# Modules to control actions in the system.
import sys
import platform
import os

# Modules to send email
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

# Class to control of structure of project
class ProgramControl(object):
    '''
    asdfsadfsadfsadfsadfsadfsadfsad
    '''
    def __init__(self):
        '''
        Dictionary to save Countries and capitals.
        '''
        self.paises = {}

    def wipe_screen(self):
        '''
        Method that allows clear the screen from the terminal.
        We use "cls" for WINDOWS or "reset" for MAC.
        '''
        if platform.system == 'Windows': # Check the OS we use.
            os.system('cls')
        else:
            os.system('reset')

    def has_numbers(self, input_string):
        '''
        This method check if a string contain letters.
        '''
        return any(char.isdigit() for char in input_string)

    def function_country(self):
        '''
        Method that handles the saving of the country with it's capital.
        '''
        while True: #This while allows repeat if necessary.
            self.wipe_screen()
            print '\n' + '=' * 40
            print '=== Save Your Countries and Capitals ==='
            print '=' * 40

            # This "Try" verifies the operation to enter countries with their capital.
            try:
                # Request revenues by user.
                str_country = raw_input('\nEnter Name of Country: ')
                str_capital = raw_input('Enter Name of Capital: ')

                # Checks if the user inputs are empty.
                if str_country == ''  and str_capital == '':
                    print '\n' + '#' * 56
                    print '## Enter text for the country and the capital please. ##'
                    print '#' * 56
                    raw_input("\n\nPress enter to continue..'")
                    self.function_country()
                elif str_country == '':
                    print '\n' + '#' * 40
                    print '## Enter text for the country please. ##'
                    print '#' * 40
                    raw_input("\n\nPress enter to continue..'")
                    self.function_country()
                elif str_capital == '':
                    print '\n' + '#' * 40
                    print '## Enter text for the capital please. ##'
                    print '#' * 40
                    raw_input("\n\nPress enter to continue..'")
                    self.function_country()

                # Control for the entry of the country.
                if self.has_numbers(str_country) == False:
                    pass
                else:
                    print '\n'+'#' * 44
                    print u'## The country name can\'t contain numbers ##'
                    print '#' * 44
                    raw_input("\n\nPress enter to continue...")
                    self.function_country()

                # Control for the entry of the capital.
                if self.has_numbers(str_capital) == False:
                    pass
                else:
                    print '\n'+'#' * 44
                    print u'## The capital name can\'t contain numbers ##'
                    print '#' * 44
                    raw_input("\n\nPress enter to continue...")
                    self.function_country()
            except ValueError as catch_error:
                print catch_error
                raw_input("\n\nPress enter to continue...")

            try:
                # Process for saving countries
                str_country = str_country.title()
                str_capital = str_capital.title()
                self.paises[str_country] = str_capital

                print '\n' + '=' * 53
                print '= Thank you for adding a country with it\'s capital. ='
                print '=' * 53

                raw_input("\n\nPress enter to continue...")
                self.wipe_screen()
                self.run()
            except ValueError:
                print '\n' + '#' * 55
                print '## Error occurred, please try again and if the error ##'
                print '## continues, contact the administrator              ##'
                print '#' * 55
                raw_input("\n\nPress enter to continue...")
                self.run()

    def print_contries(self):
        '''
        Method to display the list of countries.
        '''
        self.wipe_screen()
        print '\n' + '=' * 31
        print '=      List of countries      ='
        print '=' * 31 +'\n'

        for key in self.paises.keys():
            print str(key)

        raw_input("\n\nPress enter to continue...")
        self.wipe_screen()

    def print_capitals(self):
        '''
        Method to display the list of capitals.
        '''
        self.wipe_screen()
        print '\n' + '=' * 30
        print '=      List of capitals      ='
        print '=' * 30 +'\n'

        for key in self.paises.keys():
            print self.paises[key]

        raw_input("\n\nPress enter to continue...")
        self.wipe_screen()

    def print_all(self):
        '''
        Method to display the list of country and their capitals.
        '''
        self.wipe_screen()
        print '\n' + '=' * 51
        print '=      List of countries with their capitals      ='
        print '=' * 51 +'\n'

        for key, item in self.paises.items():
            print str(key) + ' : ' + str(item)

        raw_input("\n\nPress enter to continue...")
        self.wipe_screen()

    def print_all_order_by_capitals(self):
        '''
        Method to display the list of countries with their capitals sorted by capital.
        '''
        self.wipe_screen()
        print '\n' + '=' * 36
        print '=  List of countries and capitals  ='
        print '=       Oreder by Capitals         ='
        print '=' * 36 +'\n'

        # Temporary dictionary that will store as key capitals.
        json_capitales = {}

        for key, item in self.paises.items():
            json_capitales[item] = key # Save the item as key and the key as item.

        # Sorted(json_capitales.iterkeys()) can sort the capitals
        # In the dictionary before being displayed.
        for key in sorted(json_capitales.iterkeys()):
            print "%s : %s" % (json_capitales[key], key)

        raw_input("\n\nPress enter to continue...")
        self.wipe_screen()

    def send_mail_all(self):
        '''
        Method to send by email the countries and capitals.
        '''
        username = 'garcialudwin10@gmail.com'
        password = 'Cognits2014'

        toaddrs = 'lgarcia@cognits.co'
        body = 'Countries and Capitals: \n'

        # This loop creates the body of the email.
        for key, item in self.paises.items():
            body += '\n'+ str(key) + ' : ' + str(item)

        # Forming the body of email
        msg = MIMEMultipart()
        msg['From'] = username
        msg['To'] = toaddrs
        msg['Subject'] = "Countries and capitals by Ludwin Garcia"
        msg.attach(MIMEText(body, 'plain'))

        # This try controls if the email was sent
        try:
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.starttls()
            server.login(username, password)
            text = msg.as_string()
            server.sendmail(username, toaddrs, text)
            server.quit()
            print '\n' + '=' * 32
            print '= The email was sent correctly ='
            print '=' * 32
            raw_input("\n\nPress enter to continue...")
        except ValueError:
            print '\n' + '#' * 55
            print '## Error occurred, please try again and if the error ##'
            print '## continues, contact the administrator              ##'
            print '#' * 55
            raw_input("\n\nPress enter to continue...")

    def print_main_menu(self):
        '''
        Method to show main menu.
        '''
        self.wipe_screen()
        print '\n'
        print '='*65
        print '='+' '*26 + ' Main Menu '+' '*26 + '='
        print '='*65
        print '''
            \r You can choose the following options,
            \r please type the name and press enter.\n
            \r  *  "Country"
            \r      -With this option you can add Countries.'\n
            \r  *  "Countries"
            \r      -With this option you show countries.'\n
            \r  *  "Capitals"
            \r      -With this option you show capitals.'\n
            \r  *  "All"
            \r      -With this option you show Country and capitals.'\n
            \r  *  "AllOrdered"
            \r      -With this option you show Country and capitals 
            \r      -ordered alphabetical by capitals'\n
            \r  *  "AllMail" 
            \r      -With this option you can send email with the
            \r      -list of Countries and Capitals'\n
            \r  *  "exit" 
            \r      -With this option you can stop application and get out'\n
        '''
        print '=' * 65 + '\n'

    def get_menu_choice(self, main_menu):
        '''
        Method to get choice of user and verifies if choice is correctly.
        '''
        while True:
            self.print_main_menu()
            user_input = raw_input('Please type option: ')
            user_input = user_input.lower()

            try:
                # Verify if user input contains numbers.
                if self.has_numbers(user_input) == False:
                    #Verify if user input exist in the dictionary.
                    if user_input in main_menu.keys():
                        return user_input
                    else:
                        print '\n' + '#' * 57
                        print "## You can only choice menu options, please try again. ##"
                        print '#' * 57
                        raw_input('\nPress enter to continue...')
                else:
                    print '\n' + '#' * 51
                    print "## You only can enter letters, please try again. ##"
                    print '#' * 51
                    raw_input('\nPress enter to continue...')
            except ValueError as catch_error:
                print catch_error

    def exit(self):
        '''
        Method that allows exit from application.
        '''
        print '\n' + '*' * 19
        print '** See you soon! **'
        print '*' * 19
        raw_input("\n\nPlease press enter to exit...")
        self.wipe_screen()
        sys.exit(0)

    def run(self):
        '''
        This method controls the calls of methods, inside of class.
        '''

        main_menu = {
            'country': self.function_country,
            'countries': self.print_contries,
            'capitals': self.print_capitals,
            'all': self.print_all,
            'allordered': self.print_all_order_by_capitals,
            'allmail': self.send_mail_all,
            'exit': self.exit
        }

        try:
            while True:
                choice = self.get_menu_choice(main_menu)
                main_menu[choice]()
        except KeyboardInterrupt:
            print '\n' + '#' * 55
            print '## Error occurred, please try again and if the error ##'
            print '## continues, contact the administrator              ##'
            print '#' * 55
            sys.exit(0)

def main():
    '''
    In this method creates the object and runs the application.
    '''
    object_program = ProgramControl()
    object_program.run()

# Verify if application running by self.
if __name__ == '__main__':
    main()
