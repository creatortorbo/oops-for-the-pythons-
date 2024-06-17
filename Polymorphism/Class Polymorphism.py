class viahal :
   def __init__(self,fist_name,second_name):
      self.fist_name = fist_name 
      self.second_name = second_name

   def collage(self):
      print('In collage')
   
class Aman :
   def __init__(self,fist_name,second_name):
      self.fist_name = fist_name
      self.second_name = second_name

   def collage(self):
      print('In collage')
   

class Deepack :
   def __init__(self,fist_name,second_name):
      self.second_name = second_name 
      self.fist_name = fist_name 
   def collage (self):
      print('Not collage')
   
name1 = viahal('Viahal','singh')
name2 = Aman('Aman','Saw')
name3 = Deepack('Deepack','Saw')

# print(name1.fist_name,name1.second_name)
# print(f'printing the fist and second name',':',{name2.fist_name,name2.second_name}) 
# print(f'pring the fist and the second name',':',{name3.fist_name,name3.second_name})
# # print(name1.second_name)

for x in (name1,name2,name2):
   x.collage()