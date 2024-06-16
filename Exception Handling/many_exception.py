# here in this code to many exception and we handing error 
try:
 print(x)

except NameError:
  print('variable x is not defined')

except :
  print('Something else went wrong')