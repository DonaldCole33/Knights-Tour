'''
Created on Feb 2, 2015

@author: Don Cole
'''
#!/usr/bin/env python

from heapq import heappush, heappop # for priority queue
import string
import pickle

"""pdb.set_trace()
    b: set a breakpoint
    c: continue debugging until you hit a breakpoint
    s: step through the code
    n: to go to next line of code
    l: list source code for the current file (default: 11 lines including the line being executed)
    u: navigate up a stack frame
    d: navigate down a stack frame
    p: to print the value of an expression in the current context"""



class Node (object):
    def __init__(self, row=None, column=None, choiceNum=None):
        self.row = row
        self.column = column
        self.choiceNum = choiceNum
        self.nextNode = None
        self.head = None
        
    def printList(self):
        #num is passed, it will only print that node's info
        #otherwise it will print all nodes
        current = self.head
        while current is not None:
                print "initial condition", current.choiceNum, "(",current.row+1,",",current.column+1,")"
                current = current.nextNode
            
    def insert(self, node):
        if self.head == None:
            self.head = node
        else:
            # set new nodes pointer to old head
            node.nextNode = self.head
            # reset head to new node
            self.head = node
            
    def search(self, num):
        current = self.head
        if current.choiceNum == num:
            return self.head
            current = current.nextNode
        else:
            while current:
                if current.choiceNum == num:
                    return current
                else:
                    current = current.nextNode
            print "Node not in Linked List"
            
            
    def edit(self, num):
        current = self.head
        if current == None:
            print "Node not in Linked List"
            return
        elif current.choiceNum == num:
            print "Please select your new starting row on the 8x8 chess board."
            current.row = input("Row:")
            int(current.row)
            
            while (current.row < 1 or current.row > N):
                print "Please input an integer between 1 and", N
                current.row = input("Row:")
                int(current.row)
            
            current.row -= 1
            
            print "Please select your new starting column on the 8x8 chess board. "
            current.column = input("Column:")
            int(current.column)
            while (current.column < 1 or current.column > N):
                print "Please input an integer between 1 and", N
                current.column = input("Column:")
                int(current.column)
    
            current.column -= 1
            current = current.nextNode
        else:
            while current:
                if current.choiceNum == num:
                    print "Please select your new starting row on the 8x8 chess board."
                    current.row = input("Row:")
                    int(current.row)
                    
                    while (current.row < 1 or current.row > N):
                        print "Please input an integer between 1 and", N
                        current.row = input("Row:")
                        int(current.row)
            
                    current.row -= 1
            
                    print "Please select your new starting column on the 8x8 chess board. "
                    current.column = input("Column:")
                    int(current.column)
                    while (current.column < 1 or current.column > N):
                        print "Please input an integer between 1 and", N
                        current.column = input("Column:")
                        int(current.column)
            
                    current.column -= 1
                    return
                else:
                    current = current.nextNode    
        print "Node not in Linked List"
        
    def size(self):
        current = self.head
        size = 0
        while current is not None:
            size += 1
            current = current.nextNode
        return size
    
    def delete(self, num):
        if self.size() == 0:
            print "List is empty."
            return
        else:
            current = self.head
            previous = None
            found = False
            while not found:
                if current is None:
                    print "Node not in Linked List"
                    return
                elif current.choiceNum == num:
                    found = True
                else:
                    previous = current
                    current = current.nextNode
            #Deleting Found node
            if previous is None:
                self.head = current.nextNode
            else:
                previous.nextNode = current.nextNode

    def add(self, choiceNum):
        newnode = Node(0,0,choiceNum)
        
        print "Please select your starting point on the 8x8 chess board."
        newnode.row = input("Row:")
        
        while (newnode.row < 1 or newnode.row > N):
            print "Please input an integer between 1 and", N
            newnode.row = input("Row:")
        
        newnode.row -= 1
        
        newnode.column = input("Column:")
        while (newnode.column < 1 or newnode.column > N):
            print "Please input an integer between 1 and", N
            newnode.column = input("Column:")
        
        newnode.column -= 1
        
        self.insert(newnode)
        
def main():
    global N
    N = 8    #create the global Variable for N = 8 (8x8 chess board)
    i = 1
    initList = Node()   #initialization of linked list
    
    print "Welcome to Don's Knights Tour Program"
    
    #opens a file for output
    logFile = open("KTlogfile.txt", "w")
    logFile.write("Log File for Knight's Tour Program\n")
    
    while True:
        print "Please select your starting point on the 8x8 chess board."
        startRow = input("Row:")
        int(startRow)
        while (startRow < 1 or startRow > N):
            print "Please input an integer between 1 and", N
            startRow = input("Row:")
            int(startRow)
        
        startRow -= 1
        
        startColumn = input("Column:")
        int(startColumn)
        while (startColumn < 1 or startColumn > N):
            print "Please input an integer between 1 and", N
            startColumn = input("Column:")
            int(startColumn)
            
        startColumn -= 1
        
        #write to file
        logFile.write('initial Condition '+str(i)+' ('+str(startRow)+','+str(startColumn)+')\n')
        
        #insert init conditions to list
        newNode = Node(startRow, startColumn, i)
        initList.insert(newNode)
        i += 1
        
        print"Would you like to enter another Initial Condition?"
        init = raw_input("Enter Y for Yes, N for No:")
        while (init != "Y") and (init != "y") and (init != "N") and (init != "n"):
            print "Please enter N or Y."
            init = raw_input("Enter Y for Yes, N for No: ")
        
        if (init == "y") or (init == "Y"):
            continue
        else:
            break
    logFile.write("End of First Entered Initial Conditions\n")
    
    while True:    
        print "***Menu***"
        print "1 - Print Initial Conditions"
        print "2 - Add an Initial Condition"
        print "3 - Delete an Initial Condition"
        print "4 - Edit an Initial Condition"
        print "5 - Solve the Knight's Tour with the current Initial Conditions"
        print "0 - Quit"
        selectionVar = input("Selection: ")
                
        if (selectionVar == 1):
            initList.printList()
            logFile.write("User Selected Print List\n")
        if (selectionVar == 2):
            logFile.write("User added Initial Condition\n")
            initList.add(i)   
            i+=1 
        elif (selectionVar == 3):
            print"Which Initial Condition would you like to delete?"
            num = input("Enter the integer: ")
            logFile.write("User Deleted Initial Condition "+str(num)+"\n")
            initList.delete(num)
        elif (selectionVar == 4):
            print "Which Initial Condition would you like to edit?"
            num = input("Enter the integer: ")
            logFile.write("User Edited Initial Condition "+str(num)+"\n")
            initList.edit(num)
        elif (selectionVar == 5):
            #solve the KT
            print"Solving..........."
            print
            solveTour(initList.head, logFile)
            print "Thanks for playing Knight's Tour By Don Cole!"
            logFile.write("Done\n")
            logFile.close()
            break
        elif (selectionVar == 0):
            print "Goodbye!"
            logFile.write("User Quit\n")
            logFile.close()
            break
        else:
            print "Please Select a Menu Option."
    
    """This function determines whether or not the next move 
    is valid or not
    Returns a 1 if it is ok
    Returns a 0 if it is not"""
    
def isSafe (row, column, array):
    
    if ((row >= 0 and row < N) and (column >= 0 and column < N) and (array[row][column] == -1)):
        return 1
    return 0
    
    """This function solves the Knight Tour problem using Backtracking and 
    Warnsdoff's Rule.  solvKTUtil is the function that implements backtracing
    The function returns false if no complete tour is possible, otherwise it
    returns true and prints the tour."""
def solveTour (node, file):
    current = node
    
    while (current):
        row = current.row
        column = current.column
        
        #initialize solution double array with 0 values 
        solution = [[-1 for i in range(8)] for i in range(8)]
     
        """rowMove[] and columnMove[] define next move of Knight.
           rowMove[] is for next value of row coordinate
           columnMove[] is for next value of column coordinate """
        rowMove = ( 2, 1, -1, -2, -2, -1,  1,  2 )
        columnMove = ( 1, 2,  2,  1, -1, -2, -2, -1 )
        
        #Start the knight out using Warnsdoff's Rule
        #returns an array back the current variables
        #ei - variables = (row, column, solution)
        variables = warnsdoff(row, column, solution, rowMove, columnMove)
        row = variables[0]
        column = variables[1]
        solution= variables[2]
        
        #printBoard(current, solution)
        
        # Start from row,column and explore all tours using solveBacktracking()
        if (solveBacktracking(row, column, 32, solution, rowMove, columnMove) == False):
            print("Solution does not exist")
            file.write("Initial Condition "+str(current.choiceNum)+" ("+str(current.row)+","+str(current.column)+")\n")
            file.write("Solution does not Exist\n")
        else:
            file.write("Initial Condition "+str(current.choiceNum)+" ("+str(current.row)+","+str(current.column)+")\n")
            printBoard(current, solution, file)
            
        current = current.nextNode
        
"""Utility for solving the Knights tour problem with backtracking."""
def solveBacktracking(row, column, movei, solution, rowMove, columnMove):
    
    if (movei == N*N):
        return True

    # Try all next moves from the current coordinate row, column
    for i in range(8):
        next_row = row + rowMove[i]
        next_column = column + columnMove[i]
        
        if (isSafe(next_row, next_column, solution)):
            solution[next_row][next_column] = movei
            
            if (solveBacktracking(next_row, next_column, movei+1, solution, rowMove, columnMove) == True):
                return True
            else:
                solution[next_row][next_column] = -1; #backtracking
    
    return False
   
def warnsdoff(row, column, solution, rowMove, columnMove): 

    for k in range(31):
        solution[row][column]  = k
        nextMoves = []  #array for the next moves
        for i in range(8):
            next_row = row + rowMove[i]; 
            next_column = column + columnMove[i]
            if isSafe(next_row, next_column, solution):
            #if next_row >= 0 and next_row < N and next_column >= 0 and next_column < N:
                #if solution[next_row][next_column] == -1:
                # count the available neighbors of the neighbor
                counter = 0
                for j in range(8):
                    next_next_row = next_row + rowMove[j] 
                    next_next_column = next_column + columnMove[j]
                    if isSafe(next_next_row, next_next_column, solution):
                    #if next_next_row >= 0 and next_next_row < N and next_next_column >= 0 and next_next_column < N:
                    #    if solution[next_next_row][next_next_column] == -1: 
                        counter += 1
                heappush(nextMoves, (counter, i))
        # move to the neighbor that has min number of available neighbors
        if len(nextMoves) > 0:
            (p,m) = heappop(nextMoves)
            row += rowMove[m]
            column += columnMove[m]
        else: break
        
    #completing the last move for this function 
    solution[row][column] = k+1    
    return (row, column, solution)    

def printBoard(node, array, file):
    current = node
    solution = array
    # print the Chess Board
    print "Initial Condition", current.choiceNum,"(",current.row+1,",",current.column+1,")"
    for printRow in range(N):
        for printColumn in range(N):
            print string.rjust(str(solution[printRow][printColumn]), 2),
            file.write(str(solution[printRow][printColumn]))
            file.write("|")
        print
        file.write("\n")
    print
    file.write("\n")
if __name__ == '__main__':main()



    