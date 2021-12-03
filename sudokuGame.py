
def __main__():
    col_id_Sudoku = "ABCDEFGHI" ## Column reference

    vars = {} ## Save the data boxes 

    sudoku01 = "sample_data/sudoku01.txt" ## Data reference 

    constRow = [] ## Save row, window and column constraints
    constColumn = []
    constWin = []

    defFullVars(vars, col_id_Sudoku)

    loadData(vars, sudoku01, col_id_Sudoku)

    setAllDiffConstraints(constRow, constColumn, constWin, col_id_Sudoku)
    
    drawBoard(vars, col_id_Sudoku)

def defFullVars(vars, cis): ## Create the boxes extructure
    for i in cis:
        for j in range(1,10):
            vars[str(i)+str(j)] = set(range(1,10))

def setValue(vars, name, value): ## Change number of a box
    vars[name]={value}

def loadData(vars, sdk01, cis): ## Load values form referece file
    file1 = open(sdk01, "r")

    for i in range(1,10):
        for j in cis:
            cur = int(file1.readline())

            if(cur < 10):
                setValue(vars,str(j)+str(i),cur)

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


def setAllDiffConstraints(constRow, constColumn, constWin, cis):
  rowConstraints(constRow, cis)

  colConstraints(constColumn, cis)
  
  for i in range(3):
    for j in range(3):
      winConstraints(constWin,i,j, cis)

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