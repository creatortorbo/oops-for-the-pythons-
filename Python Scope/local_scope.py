# A variable created inside a function is available inside that function
def my_fun():
   x = 100
   print(f'The value of x',':',x)

my_fun()