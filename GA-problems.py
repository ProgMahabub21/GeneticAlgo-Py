import random

individuals = ['01101','11000','01000','10011']
    

def  computePhenotype(individuals):

    decoded =[]

    n = len(individuals)

    decoded = [int(individuals[j],2) for j in range(n)]
  
    
    return decoded

phenotypes = computePhenotype(individuals)
    
print('Decoded Phenotypes: ',phenotypes)           #phenotypes being calculated from chromosome

def computefitness(phenotypes) :

    fitness = []
    for i in phenotypes:
     fitness.append(i*i)
    return fitness
   # return fitness

fitval =computefitness(phenotypes)    
print('Calculated fitness: ',fitval)    


def computeProb(fitval) :
    prob =[]
    totalfitness = sum(fitval)
    for x in fitval:
        prob.append(round(round(x/totalfitness,3),2))
       # print(x)
      #  prob.append(x/totalfitness)
    return prob    

ShowProb = computeProb(fitval)

print('Total fitness: ',sum(fitval))
print('Probability of each : ',ShowProb)

# Part 2 bin create
 
def associateBin(ShowProb):
    
    init =0.00 # initial prob is 0
    i =0
    aBin = []
    while( i < len(ShowProb)):
        aBin.append((init,(ShowProb [i] + init)))
        init += ShowProb[i]
        i+=1
    return aBin        

TableBin = associateBin(ShowProb)
print('Associated Bin Tuple',TableBin) 


# Part 3 Choice String based on given random value
def StringSelection(TableBin):

    Selection = []
    for i in range(len(individuals)):
        randValue = round(random.uniform(0, 1), 2)
        print("Choosen random value(float): ",randValue)
        for i, j in enumerate(TableBin):
            # print()

            if(randValue > j[0] and randValue < j[1]):
                Selection.append(individuals[i])
    return Selection

def StringSelection1(TableBin):
    randValue =[]
    Selection = []
    k=0
    for i in range(len(individuals)):
        randValue[k] = round(random.uniform(0, 1), 2)
        print(f"Choosen random value(float): {randValue}")
        k+=1

    while(k in range(len(individuals))):
        for i, j in enumerate(TableBin):
            # print()

             if(randValue[k] > j[0] and randValue[k] < j[1]):
                  Selection.append(individuals[i])
        k+=1
                  
      
          
    return Selection


chosenStrings = StringSelection(TableBin)

print(chosenStrings)