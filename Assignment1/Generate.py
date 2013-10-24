import random

def RandString(length):
   string = ''                # Nothing yet
   for i in range(length):
      string = string + str(unichr(random.randint(32,127)))
   return string

