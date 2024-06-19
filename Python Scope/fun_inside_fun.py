# The local variable can be accessed from a function within the function
def my_fun ():
  x = 300
  def inner_fun():
       print('The printing the value of x is :',x)
  inner_fun()
  

my_fun()