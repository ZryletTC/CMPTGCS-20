# tempConversions.py   A module for converting between fahrenheit and celsius

def fToC(ftemp):
      ''' convert fahrenheit to celsius '''
      return (ftemp-32.0)/1.8

def cToF(ctemp):
      ''' convert celsius to fahrenheit '''
      return (ctemp*1.8)+ 32.0
