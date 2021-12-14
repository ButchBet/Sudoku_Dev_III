
def __main__():
  col_id_Sudoku = "ABCDEFGHI" ## Column reference

  vars = {} ## Save the data boxes 
  varAux = {}

  sudoku01 = "sample_data/sudoku02.txt" ## Data reference 

  constraints = [] ## Save row, window and column constraints

  varWithValues = [] ## Save the variables that have just one value (In the begining)
  # varWithValues2 = [] ## Save the variables that have just one value (While the program runs)

  trys = 0 ## Save the numbers of iteratiosn of the infinity loop 

  defFullVars(vars, col_id_Sudoku)

  loadData(vars, sudoku01, col_id_Sudoku)

  setAllDiffConstraints(constraints, col_id_Sudoku)

  varAux = vars

  findConsistency(vars, constraints, varWithValues, col_id_Sudoku)

  if(len(varWithValues) != 81):
    searching(vars, constraints, varWithValues, col_id_Sudoku)

  # print()
  # print("Begining")
  # drawBoard(varsAux, cis)
  
  # print()
  # print("End")
  # drawBoard(vars, cis)
  # print()
  # print("Number of trys: " + str(trys))
  # print()
  # print("Size of the list: " + str(len(varWithValues)))




def defFullVars(vars, cis): ## Create the boxes extructure
  for i in cis:
      for j in range(1,10):
          vars[str(i)+str(j)] = set({})

def setValue(vars, name, value): ## Change number of a box
  vars[name]={value}

def setMultipelValues(vars, name, value): ## Change multiple posible numbers of a box
  vars[name].add(value)

def loadData(vars, sdk01, cis): ## Load values form referece file
  file1 = open(sdk01, "r")

  for i in range(1,10):
      for j in cis:
          cur = int(file1.readline())

          if(cur < 10):
              setValue(vars,str(j)+str(i),cur)
          else:
              for k in str(cur):
                setMultipelValues(vars, str(j)+str(i),int(k))

def setConstraintDiff(const,arity,varList):
  const.append([arity]+varList)

def rowConstraints(const, cis):
  for i in range(1,10):
    l=[]

    for j in cis:
      l.append(str(j)+str(i))

    setConstraintDiff(const,9,l)

def colConstraints(const, cis):
  for i in cis:
    l=[]

    for j in range(1,10):
      l.append(str(i)+str(j))

    setConstraintDiff(const,9,l)

def winConstraints(const,r,c, cis):
  winLen=3

  cis=cis[(c*winLen):((c*winLen)+winLen)]

  rowsIndex=list(range(((r*winLen)+1),((r*winLen)+(winLen+1))))

  l=[]

  for i in rowsIndex:
    for j in cis:
      l.append(str(j)+str(i))

  setConstraintDiff(const,9,l)


def setAllDiffConstraints(const, cis):
  rowConstraints(const, cis)

  colConstraints(const, cis)
  
  for i in range(3):
    for j in range(3):
      winConstraints(const,i,j, cis)

def setVarWithValues(vars, varWithValues):
  for k,v in vars.items():
      if(len(v)==1):
          varWithValues.append(k)

def mainConsistency(vars, constraints, varWithValues):
  for i in varWithValues:
      for j in constraints:
          if(i in j):
              # print("vamos a reducir de la variables asociadas en la restriccion "+str(j)+" el valor de la variable "+i+" que es "+str(list(vars[i])[0]))
              for k in j[1:]:
                  if(k!=i):
                      # print("..eliminando el valor mencionado del dominio de la variable "+k+" que es "+str(vars[k]))
                      vars[k].discard(list(vars[i])[0])
      # print(vars)

def findConsistency(vars, constraints, varWithValues, cis):
  size = len(varWithValues)

  trys = 0

  while True:
      trys += 1
      setVarWithValues(vars, varWithValues)

      mainConsistency(vars, constraints, varWithValues)  

      if(len(varWithValues) == size): 
        break
      else:
        size = len(varWithValues)
        
      varWithValues = []

##Chronological Backtracking
def searching(vars, constraints, varWithValues, cis):
  aux = vars

  # print(aux)
  # print(vars)

  for i in range(1, 10):
    for j in cis:
      replaceList = list(vars[cis[cis.find(j)] + str(i)])

      if(len(replaceList) > 1):
        vars[cis[cis.find(j)] + str(i)] = replaceList[0]

        replaceList.pop(0)

        aux[cis[cis.find(j)] + str(i)] = set(replaceList)

        # print(cis[cis.find(j)] + str(i) + " --> " + str(aux[cis[cis.find(j)] + str(i)]))

        findConsistency(vars, constraints, varWithValues, cis)

        if(len(varWithValues) != 81):
          searching(vars, constraints, varWithValues, cis)
        else:
          break


def drawBoard(vars, cis):
    concat = ""

    for j in range(1,10):
        for k in cis:
            if((k == 'D')| (k == 'G')):
                concat += "  "

            if(len(vars[k+str(j)]) == 1):
                concat += " " + str(*vars[k+str(j)])
            else:
                concat += " 0"
    
        print(concat)

        if((j == 3) | (j ==6)):
            print("")

        concat = ""

if __name__ == "__main__":
    __main__()