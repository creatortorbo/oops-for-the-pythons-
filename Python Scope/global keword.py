# here we can accesing the varible in the local with the golbal keyword 
def my_func():
  global x
  x = 100

my_func()

print(x)