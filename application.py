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

# Dictionary for control access to the functions
MAIN_MENU = [u'1)  Ingresar País con su Capital',
            u'2)  Ver lista de países',
            '3)  Ver lista de capitales',
            '4)  Ver Todo',
            '5)  Ver todo ordenado por capital',
            '6)  Enviar un Mail con todo',
            '7)  Salir']

# Clase que controla la estructura del proyecto 
class Programa(object):

  def __init__(self):
    self.paises = {} # Diccionario que almacena país y capital

  # Metodo que permitirá limpiar la pantalla de la terminal.
  # Utilizamos "cls" para WINDOWS o "reset" para MAC
  def LimpiarPantalla(self):
    if os.name == 'ce' or 'nt'or 'dos': #Verifica si el OS utilizado es Windows.
      os.system('cls') 
    else:
      os.system('reset')

  # Metodo que mostrará el Menú.
  def PrintMainMenu(self):
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

  # Metodo que mostrará el listado de países ingresados.
  def PrintPaises(self):
    self.LimpiarPantalla()
    print '\n'
    print '================================='
    print u'=      Despliege de Países      ='
    print '================================='
    print '\n'
    for key in self.paises.keys():
      print str(key) 
    raw_input("\n\nPreisone Enter para continuar...")
    self.LimpiarPantalla()

  # Metodo que mostrará el listado de capitales ingresadas.
  def PrintCapitales(self):
    self.LimpiarPantalla()
    print '\n'
    print '================================='
    print '=     Despliege de Capitales    ='
    print '================================='
    print '\n'

    for key, item in self.paises.items():
      print str(item)

    raw_input("\n\nPreisone Enter para continuar...")
    self.LimpiarPantalla()

  # Metodo que mostrará el listado de país y capitales ingresadas.
  def PrintTodo(self):
    self.LimpiarPantalla()
    print '\n'
    print '================================='
    print u'=  Despliege de País y Capital  ='
    print '================================='
    print '\n'

    for key, item in self.paises.items():
      print str(key) + ' : ' + str(item)

    raw_input("\n\nPreisone Enter para continuar...")
    self.LimpiarPantalla()

  # Metodo que mostrará el listado de país y capitales ordenado por capital.
  def PrintTodoOrdenadoCap(self):
    self.LimpiarPantalla()
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
    self.LimpiarPantalla()

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

  # Metodo  que obtendra la respuesta de lo que el usuario desea realizar.
  def GetMenuChoice(self, menu):
    max_choice = len(menu)
    while True:
      user_input = raw_input(u'Ingrese una opción: '.encode(sys.stdout.encoding))
      try:
        num = int(user_input)
      except ValueError:
        continue

      if num <= max_choice and num > 0:
        return num

  def FunctionPais(self):
    while True:
      self.LimpiarPantalla()
      print '============================'
      print u'== Realice sus Ingresos =='
      print '============================'

      try:
        strPais = raw_input(u'\nIngrese el Nombre del País: '.encode(sys.stdout.encoding))
        strPais =int(strPais)
        print '****************************************************'
        print u'** No Puede Ingresar Números Como Nombre de País **'
        print '****************************************************'
        raw_input("\n\nPreisone Enter para continuar...")
        self.FunctionPais()
        return
      except ValueError:
        pass

      try:
        strCapital = raw_input(u'Ingrese el Nombre de la Capital: ')
        strCapital =int(strCapital)
        print '*******************************************************'
        print u'** No Puede Ingresar Números Como Nombre de Capital **'
        print '*******************************************************'
        raw_input("\n\nPreisone Enter para continuar...")
        self.FunctionPais()
        return
      except ValueError:
        pass

      if strPais == ''  and strCapital == '':
         print '\n'
         print '********************************************************'
         print u'** Ingresar texto para el país y la capital por favor **'
         print '********************************************************'
         self.FunctionPais()
         return
      elif strPais == '':
           print '\n'
           print '*******************************************'
           print u'** Ingresar texto para el país por favor **'
           print '*******************************************'
           self.FunctionPais()
           return
      elif strCapital == '':
           print '\n'
           print '**********************************************'
           print u'** Ingresar texto para la capital por favor **'
           print '**********************************************'
           self.FunctionPais()
           return

      try:
        self.paises[strPais] = strCapital
        print '\n'
        print '=============================================='
        print u'= Gracias por agregar un país con su capital ='
        print '=============================================='
        raw_input("\n\nPreisone Enter para continuar...")
        self.LimpiarPantalla()
        return
      except ValueError:
        continue

  def Run(self):
    try:
      while True:
        self.PrintMainMenu()
        choice = self.GetMenuChoice(MAIN_MENU)
        if choice == 1:
            self.FunctionPais()
        elif choice == 2:
            self.PrintPaises()
        elif choice == 3:
            self.PrintCapitales()
        elif choice == 4:
            self.PrintTodo()
        elif choice == 5:
            self.PrintTodoOrdenadoCap()
        elif choice == 6:
            self.SendMailTodo()
        elif choice == 7:
            print 'Hasta pronto!\n'
            return
    except KeyboardInterrupt:
      return

def main():
  objeto = Programa()
  objeto.Run()

if __name__ == '__main__':
  main()
