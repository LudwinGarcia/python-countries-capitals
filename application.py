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
        strCountry = raw_input('\nEnter Name of Country: ')
        if strCountry.isalpha() == True:
          pass
        else:
          print '\n'+'#' * 44
          print u'## The country name can\'t contain numbers ##'
          print '#' * 44
          raw_input("\n\nPress enter to continue..'")
          self.FunctionCountry()

        # Control for the entry of the capital.
        strCapital = raw_input('Enter Name of Capital: ')
        if strCapital.isalpha() == True:
          pass
        else:
          print '\n'+'#' * 44
          print u'## The capital name can\'t contain numbers ##'
          print '#' * 44
          raw_input("\n\nPress enter to continue..'")
          self.FunctionCountry()

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

        # This try controls save entries to the dictionary.
        strCountry = strCountry.title()
        strCapital = strCapital.title()
        self.paises[strCountry] = strCapital
        print '\n' + '=' * 53
        print '= Thank you for adding a country with it\'s capital. ='
        print '=' * 53
        raw_input("\n\nPreisone Enter para continuar...")
        self.WipeScreen()
        return
      except ValueError as CatchError:
        print CatchError
        raw_input("\n\nPress enter to continue..'")

  # Metodo que mostrará el listado de países ingresados.
  def PrintContries(self):
    self.WipeScreen()
    print '\n'
    print '================================='
    print u'=      Despliege de Países      ='
    print '================================='
    print '\n'
    for key in self.paises.keys():
      print str(key) 
    raw_input("\n\nPreisone Enter para continuar...")
    self.WipeScreen()

  # Metodo que mostrará el listado de capitales ingresadas.
  def PrintCapitales(self):
    self.WipeScreen()
    print '\n'
    print '================================='
    print '=     Despliege de Capitales    ='
    print '================================='
    print '\n'

    for key, item in self.paises.items():
      print str(item)

    raw_input("\n\nPreisone Enter para continuar...")
    self.WipeScreen()

  # Metodo que mostrará el listado de país y capitales ingresadas.
  def PrintTodo(self):
    self.WipeScreen()
    print '\n'
    print '================================='
    print u'=  Despliege de País y Capital  ='
    print '================================='
    print '\n'

    for key, item in self.paises.items():
      print str(key) + ' : ' + str(item)

    raw_input("\n\nPreisone Enter para continuar...")
    self.WipeScreen()

  # Metodo que mostrará el listado de país y capitales ordenado por capital.
  def PrintTodoOrdenadoCap(self):
    self.WipeScreen()
    print '\n'
    print '================================='
    print u'=  Despliege de País y Capital  ='
    print '=      Ordenado Por Capital     ='
    print '================================='
    print '\n'

    # Diccionario temporal que almacenara como llave las capitales
    jsonCapitales = {}

    for key, item in self.paises.items():
      jsonCapitales[item] = key #Guardamos el item como key y la key como item.

    # Sorted(jsonCapitales.iterkeys()) permite ordenar las capitales
    # Del diccionario antes de ser mostradas.
    for key in sorted(jsonCapitales.iterkeys()):
       print "%s: %s" % (jsonCapitales[key],key)

    raw_input("\n\nPreisone Enter para continuar...")
    self.WipeScreen()

  # Metodo que enviara países y capitales por email.
  def SendMailTodo(self):
    username = 'garcialudwin10@gmail.com'
    password = 'Cognits2014'

    toaddrs  = 'garcialudwin@galileo.edu'
    body = 'Países y capitales: \n'

    # Este loop permite armar el body del email.
    for key, item in self.paises.items():
      body += '\n'+ str(key) + ' : ' + str(item)

    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = toaddrs
    msg['Subject'] = "Países y capitales by Ludwin Garcia"
    msg.attach(MIMEText(body, 'plain'))

    try:
      server = smtplib.SMTP('smtp.gmail.com:587')
      server.starttls()
      server.login(username,password)
      text = msg.as_string()
      server.sendmail(username, toaddrs, text)
      server.quit()
      print '\n'
      print '==================================='
      print '= El Correo Se Envio Exitosamente ='
      print '==================================='
    except:
      print '\n'
      print '======================================'
      print u'= Error Al Enviar Correo Electrónico ='
      print '======================================'

  # Method to show main menu.
  def PrintMainMenu(self):
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

  # MMethod to receive choice of user.
  def GetMenuChoice(self,MAIN_MENU):
    while True:
      self.PrintMainMenu()
      user_input = raw_input('Please type option: ')
      user_input = user_input.lower()
      try:
        if user_input.isalpha() == True:
          if user_input in MAIN_MENU.keys():
            return user_input
          else:
            print '\n' + '=' * 51
            print "You can only choice menu options, please try again."
            print '=' * 51
            raw_input('\nPress enter to continue...')
        else:
          print '\n' + '=' * 45
          print "You only can enter letters, please try again."
          print '=' * 45
          raw_input('\nPress enter to continue...')
      except ValueError as CatchError:
        print CatchError

  def Run(self):
    MAIN_MENU = {
      'country': self.FunctionCountry,
      'countries': self.PrintContries,
      'capitals': self.PrintCapitales,
      'all': self.PrintTodo,
      'allordered': self.PrintTodoOrdenadoCap,
      'allmail': self.SendMailTodo
    }
    try:
      while True:
        choice = self.GetMenuChoice(MAIN_MENU)
        if choice == 'exit':
            print 'See you soon!\n'
            raw_input("Please press enter to exit...")
            return
        else:
          MAIN_MENU[choice]()

    except KeyboardInterrupt:
      return

def main():
  objectProgram = ProgramControl()
  objectProgram.Run()

if __name__ == '__main__':
  main()