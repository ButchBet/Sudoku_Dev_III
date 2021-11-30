
def __main__():
    col_id_Sudoku = "ABCDEFGHI" ## Column reference

    vars = {} ## Save the data boxes 

    sudoku01 = "sample_data/sudoku01.txt" ## Data reference 
    
    constraints_row = [] ## Save row and column constraints
    constraints_column = []

    defFullVars(vars, col_id_Sudoku)

    loadData(vars, sudoku01, col_id_Sudoku)

    generateConstraints(constraints_row, constraints_column, col_id_Sudoku)
    
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

def setConstraintDiff(const,arity,varList): ## Set required constraints for each posible selection
    const.append([arity]+varList)

def generateConstraints(cr, cc, cis): ## Generate the list of posible constraints
    ## Rows
    for i in range(1,10):
        ListKeys = []

        for j in cis:
            ListKeys.append(j+str(i))

        setConstraintDiff(cr, 9, ListKeys) 

    ## Columns
    for i in cis:
        ListKeys = []
        
        for j in range(1,10):
            ListKeys.append(i+str(j))

        setConstraintDiff(cc, 9, ListKeys)

def drawBoard(vars, cis):
    concat = ""

    for j in range(1,10):
        for k in cis:
            if(len(vars[k+str(j)]) == 1):
                concat += " " + str(*vars[k+str(j)])
            else:
                concat += " 0"
        
        print(concat)

        concat = ""

if __name__ == "__main__":
    __main__()