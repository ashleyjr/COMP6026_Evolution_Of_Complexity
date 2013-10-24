import random

def Mutate(parent):
   child = parent                                                    # Copy the parent
   for i in range(len(child)):
      if(random.randint(1,len(child)) == (len(child))):              # If random is same length then lucky, probability 1/length
         new = str(unichr(random.randint(32,127)))
         child = child[:i] + new + child[i+1:]                       # Replace index
   return child

def Crossover(Mother,Father):
   if(len(Mother) > len(Father)):                                   # Play is safe
      length = len(Mother)
   else:
      length = len(Father)
   Child = Mother                                                    # Copy mum to start
   for i in range(length):
      if(random.randint(0,1)):
         Child = Child[:i] + Father[i] + Child[i+1:]                       # Replace index

   return Child
