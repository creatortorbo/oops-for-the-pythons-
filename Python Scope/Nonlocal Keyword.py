def my_func1():
   x = 'not hello'

   def my_func2():
     nonlocal x
     x = 'hello'
   
   my_func2()
   return x 

print(my_func1())