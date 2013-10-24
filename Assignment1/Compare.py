def String(Compare1,Compare2):            # Doesn't matter order in which strings are sent
   if(len(Compare1) > len(Compare2)):     # Play it safe
      length = len(Compare2)              # Compare2 is the shortest
   else:
      length = len(Compare1)              # Compare1 is shortest or they are the same length
   fits = 0                               # init counter
   for i in range(length):
      char1 = Compare1[i]
      char2 = Compare2[i]
      if(char1 == char2):                 # Go through chars and count snaps
         fits = fits + 1
   return fits

def GetMax(ListOfIndividuals,Perfection):
   top = 0
   for i in range(len(ListOfIndividuals)):
      temp = String(ListOfIndividuals[i],Perfection)
      if(temp > top):
         top = temp
   return top

