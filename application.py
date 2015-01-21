# -*- coding: utf-8 -*

"""
In this code you can find a possible good solution of
python-countries-capitals, these project freedom
analyze and restructure, if you find a better way
applying an area in the code, you can comment it on Github Issues
"""

# Modules to control actions in the system.
import sys
import os

# Modules to send email
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

# Class to control of structure of project
class ProgramControl(object):

  def __init__(self):
    '''
    Dictionary to save Countries and capitals.
    '''
    self.paises = {} 

  def WipeScreen(self):
    '''
    Method that allows clear the screen from the terminal.
    We use "cls" for WINDOWS or "reset" for MAC.
    '''
    if os.name == 'ce' or 'nt'or 'dos': # Check the OS we use.
      os.system('cls') 
    else:
      os.system('reset')

  def HasNumbers(self, inputString):
      '''
      This method check if a string contain letters.
      '''
      return any(char.isdigit() for char in inputString)

  def FunctionCountry(self):
    '''
    Method that handles the saving of the country with it's capital.
    '''
    while True: #This while allows repeat if necessary.
      self.WipeScreen()
      print '\n' + '=' * 40
      print '=== Save Your Countries and Capitals ==='
      print '=' * 40

      # This "Try" verifies the operation to enter countries with their capital.
      try:
        # Request revenues by user.
        strCountry = raw_input('\nEnter Name of Country: ')
        strCapital = raw_input('Enter Name of Capital: ')

        # Checks if the user inputs are empty.
        if strCountry == ''  and strCapital == '':
           print '\n' + '#' * 56
           print '## Enter text for the country and the capital please. ##'
           print '#' * 56
           raw_input("\n\nPress enter to continue..'")
           self.FunctionCountry()
        elif strCountry == '':
             print '\n' + '#' * 40
             print '## Enter text for the country please. ##'
             print '#' * 40
             raw_input("\n\nPress enter to continue..'")
             self.FunctionCountry()
        elif strCapital == '':
             print '\n' + '#' * 40
             print '## Enter text for the capital please. ##'
             print '#' * 40
             raw_input("\n\nPress enter to continue..'")
             self.FunctionCountry()

        # Control for the entry of the country.
        if self.HasNumbers(strCountry) == False:
          pass
        else:
          print '\n'+'#' * 44
          print u'## The country name can\'t contain numbers ##'
          print '#' * 44
          raw_input("\n\nPress enter to continue...")
          self.FunctionCountry()

        # Control for the entry of the capital.
        if self.HasNumbers(strCapital) == False:
          pass
        else:
          print '\n'+'#' * 44
          print u'## The capital name can\'t contain numbers ##'
          print '#' * 44
          raw_input("\n\nPress enter to continue...")
          self.FunctionCountry()
      except ValueError as CatchError: # 
        print CatchError
        raw_input("\n\nPress enter to continue...")

      try:
        # Process for saving countries
        strCountry = strCountry.title()
        strCapital = strCapital.title()
        self.paises[strCountry] = strCapital

        print '\n' + '=' * 53
        print '= Thank you for adding a country with it\'s capital. ='
        print '=' * 53

        raw_input("\n\nPress enter to continue...")
        self.WipeScreen()
        self.Run()
      except ValueError:
        print '\n' + '#' * 55
        print '## Error occurred, please try again and if the error ##'
        print '## continues, contact the administrator              ##'
        print '#' * 55
        self.Run()

  def PrintContries(self):
    '''
    Method to display the list of countries.
    '''
    self.WipeScreen()
    print '\n' + '=' * 31
    print '=      List of countries      ='
    print '=' * 31 +'\n'

    for key in self.paises.keys():
      print str(key) 

    raw_input("\n\nPress enter to continue...")
    self.WipeScreen()

  def PrintCapitals(self):
    '''
    Method to display the list of capitals.
    '''
    self.WipeScreen()
    print '\n' + '=' * 30
    print '=      List of capitals      ='
    print '=' * 30 +'\n'

    for key, item in self.paises.items():
      print str(item)

    raw_input("\n\nPress enter to continue...")
    self.WipeScreen()

  def PrintAll(self):
    '''
    Method to display the list of country and their capitals.
    '''
    self.WipeScreen()
    print '\n' + '=' * 51
    print '=      List of countries with their capitals      ='
    print '=' * 51 +'\n'

    for key, item in self.paises.items():
      print str(key) + ' : ' + str(item)

    raw_input("\n\nPress enter to continue...")
    self.WipeScreen()

  def PrintAllOrderbyCapitals(self):
    '''
    Method to display the list of countries with their capitals sorted by capital.
    '''
    self.WipeScreen()
    print '\n' + '=' * 36
    print '=  List of countries and capitals  ='
    print '=       Oreder by Capitals         ='
    print '=' * 36 +'\n'

    # Temporary dictionary that will store as key capitals.
    jsonCapitales = {}

    for key, item in self.paises.items():
      jsonCapitales[item] = key # Save the item as key and the key as item.

    # Sorted(jsonCapitales.iterkeys()) can sort the capitals
    # In the dictionary before being displayed.
    for key in sorted(jsonCapitales.iterkeys()):
       print "%s : %s" % (jsonCapitales[key],key)

    raw_input("\n\nPress enter to continue...")
    self.WipeScreen()

  def SendMailAll(self):
    '''
    Method to send by email the countries and capitals.
    '''
    username = 'garcialudwin10@gmail.com'
    password = 'Cognits2014'

    toaddrs  = 'lgarcia@cognits.co'
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
      server.login(username,password)
      text = msg.as_string()
      server.sendmail(username, toaddrs, text)
      server.quit()
      print '\n' + '=' * 20
      print '= The email was sent correctly ='
      print '=' * 20
      raw_input("\n\nPress enter to continue...")
    except:
      print '\n' + '#' * 55
      print '## Error occurred, please try again and if the error ##'
      print '## continues, contact the administrator              ##'
      print '#' * 55
      raw_input("\n\nPress enter to continue...")

  def PrintMainMenu(self):
    '''
    Method to show main menu.
    '''
    self.WipeScreen()
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
      \r  *  "Exit" 
      \r      -With this option you can stop application and get out'\n
    '''
    print '=' * 65 + '\n'

  def GetMenuChoice(self,MAIN_MENU):
    '''
    Method to get choice of user and verifies if choice is correctly.
    '''
    while True:
      self.PrintMainMenu()
      user_input = raw_input('Please type option: ')
      user_input = user_input.lower()

      try:
        # Verify if user input contains numbers.
        if self.HasNumbers(user_input) == False: 
          #Verify if user input exist in the dictionary.
          if user_input in MAIN_MENU.keys():
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
      except ValueError as CatchError:
        print CatchError

  def Exit(self):
    '''
    Method that allows exit from application.
    '''
    print '\n' + '*' * 19
    print '** See you soon! **'
    print '*' * 19
    raw_input("\nPlease press enter to exit...")
    sys.exit(0) 

  def Run(self):
    '''
    This method controls the calls of methods, inside of class.
    '''
    MAIN_MENU = {
      'country': self.FunctionCountry,
      'countries': self.PrintContries,
      'capitals': self.PrintCapitals,
      'all': self.PrintAll,
      'allordered': self.PrintAllOrderbyCapitals,
      'allmail': self.SendMailAll,
      'exit': self.Exit
    }
    try:
      while True:
        choice = self.GetMenuChoice(MAIN_MENU)
        MAIN_MENU[choice]()
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
  objectProgram = ProgramControl()
  objectProgram.Run()

# Verify if application running by self.
if __name__ == '__main__':
  main()