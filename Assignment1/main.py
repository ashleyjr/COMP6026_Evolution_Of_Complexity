##############################################################################################
# IMPORTS
##############################################################################################

import Generate                                                                                       # In same directory
import Compare
import Genetic

import random                                                                                         # Python lib



##############################################################################################
#  Static parameters
##############################################################################################

Phrase = 'methinks it is like a weasel'
NumIndividuals = 500



##############################################################################################
# Main
##############################################################################################



#############
# Initalise #
#############

print 'Input: "' + Phrase + '"'                                                                        # User output
Individuals = []

for i in range(NumIndividuals):                                                                        # Initialise the population
   Individuals.append(Generate.RandString(28))                                                         # Generate a string and add to list
   SameChars = Compare.String(Phrase,Individuals[i])                                                   # Compare the strings
   print 'Fits ' + str(SameChars) + ': ' + Individuals[i]




################
# Hill Climber #
################

#HillIndividuals = Individuals
#while(Compare.GetMax(HillIndividuals,Phrase) != len(Phrase)):                                         # Hill-climber get out clause
#   for i in range(NumIndividuals):
#      Child = Genetic.Mutate(HillIndividuals[i])                                                      # Get a child
#      NewScore = Compare.String(Child,Phrase)                                                         # Get new score
#      CurrentScore = Compare.String(HillIndividuals[i],Phrase)                                        # Get old score
#      if(NewScore > CurrentScore):
#         HillIndividuals[i] = Child                                                                   # Keep child
#         print 'Birth: ' + Child + '   Fits: ' + str(NewScore) + '  Population member: ' + str(i)
#
#



########################
# GA without crossover #
########################

#GANoCross = Individuals
#while(Compare.GetMax(GANoCross,Phrase) != len(Phrase)):
#   A = random.randint(1,len(GANoCross)-1)                                                             # Pick random individual
#   B = A
#   while(B == A):                                                                                     # Make sure not to pick the same individual for tournament
#      B = random.randint(1,len(GANoCross)-1)
#   FitnessA = Compare.String(GANoCross[A],Phrase)
#   FitnessB = Compare.String(GANoCross[B],Phrase)
#   if(FitnessA > FitnessB):                                                                           # Compare fitness, A if A > B, B if B >= A
#      GANoCross[B] = Genetic.Mutate(GANoCross[A])                                                     # Replace weaker of the two with child
#      Parent = GANoCross[A]
#      Child = GANoCross[B]
#   else:
#      GANoCross[A] = Genetic.Mutate(GANoCross[B])
#      Parent = GANoCross[B]
#      Child = GANoCross[A]
#   print 'Birth: ' + Child + '  Parent: ' + Parent
#
#



#####################
# GA with crossover #
#####################


GACross = Individuals
count = 0
while(Compare.GetMax(GACross,Phrase) != len(Phrase)):

   # Get parent 1
   A = random.randint(1,len(GACross)-1)                                                             # Pick random individual
   B = A
   while(B == A):                                                                                     # Make sure not to pick the same individual for tournament
      B = random.randint(1,len(GACross)-1)
   FitnessA = Compare.String(GACross[A],Phrase)
   FitnessB = Compare.String(GACross[B],Phrase)
   if(FitnessA > FitnessB):                                                                           # Compare fitness, A if A > B, B if B >= A
      Parent1 = GACross[A]
   else:
      Parent1 = GACross[B]


   # Repeat for parent two
   A = random.randint(1,len(GACross)-1)                                                             # Pick random individual
   B = A
   while(B == A):                                                                                     # Make sure not to pick the same individual for tournament
      B = random.randint(1,len(GACross)-1)
   FitnessA = Compare.String(GACross[A],Phrase)
   FitnessB = Compare.String(GACross[B],Phrase)
   if(FitnessA > FitnessB):                                                                           # Compare fitness, A if A > B, B if B >= A
      Parent2 = GACross[A]
   else:
      Parent2 = GACross[B]

   # Give birth

   Cross = Genetic.Crossover(Parent1,Parent2)
   Child = Genetic.Mutate(Cross)


   # Tornament two
   A = random.randint(1,len(GACross)-1)                                                             # Pick random individual
   B = A
   while(B == A):                                                                                     # Make sure not to pick the same individual for tournament
      B = random.randint(1,len(GACross)-1)
   FitnessA = Compare.String(GACross[A],Phrase)
   FitnessB = Compare.String(GACross[B],Phrase)
   if(FitnessA > FitnessB):                                                                           # Compare fitness, A if A > B, B if B >= A
      GACross[B] = Child
   else:
      GACross[A] = Child

   count = count + 1
   print ''
   print str(count)
   print 'Mother: ' + Parent1
   print 'Father: ' + Parent2
   print ' Child: ' + Child

