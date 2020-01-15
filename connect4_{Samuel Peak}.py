"""
Samuel Peak
10301770
"""
from copy import deepcopy # you may use this for copying a board

def newGame(player1,player2):
    game = {
            'player1' : player1,
            'player2' : player2,
            'who' : 1,
            'board' : [ [0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0] ]
            }
    return game
"""Creates a dictionary stating a blank 7 by 6 board. 
The names of player1 and player2 are set from the input of the function. 
Turn is 1 so player1 will start"""
def printBoard(board):
    print("\n|1|2|3|4|5|6|7|")
    print("+-+-+-+-+-+-+-+")
    for y in range (0,6):
        for x in range(0,7):
            if board[y][x]==1:
               print("|O", end ="")
            elif board[y][x]==2:
               print("|X", end ="")
            else:
                print("| ", end ="")
            if x==6:
                print("|")
"""First prints the upper template which is always the same, then cycles 
throughevery element in board and prints X O or space with a border on the same
line, on the last column print a border so the next print is on another line."""                
def getValidMoves(board):
    moves=[]
    for x in range(0,7):
        if board[0][x]==0:
            moves.append(x)
    return(moves)
"""checks all of the top row to check if a counter can be placed in each column"""    
def makeMove(board,move,who):
    for y in range (5,-1,-1):
        if (board[y][move]==0):
            board[y][move]=who
            return(board)
"""Checks from bottom if the move column has an empty slot (0) then replaces it
with the players (who) counter"""
def hasWon(board,who):
    count=0
    """horizontal 4 in a rows"""
    for y in range (0,6):
        for x in range(0,7):
            if board[y][x]==who:
                count+=1
            else:
                count=0
            if count==4:
                return True
        count=0
    """vertical 4 in a rows"""
    for x in range (0,7):
        for y in range(0,6):
            if board[y][x]==who:
                count+=1
            else:
                count=0
            if count==4:
                return True
        count=0
    """diagonal right (\) (L to R) 4 in a rows"""
    diag_R=[[0,2,4],[0,1,5],[0,0,6],[1,0,6],[2,0,5],[3,0,4]]
    """diag[diagona[start x,start y, length (number of elements to check)]]"""
    for dr in range (0,6):
        count=0
        for i in range(0,diag_R[dr][2]):
            x=diag_R[dr][0]+i
            y=diag_R[dr][1]+i
            if board[y][x]==who:
                count+=1
            else:
                count=0
            if count==4:
                return True
        count=0    
    """diagonal left (/) (R to L) 4 in a row"""
    diag_L=[[3,0,4],[4,0,5],[5,0,6],[6,0,6],[6,1,5],[6,2,4]]
    for dl in range (0,6):
        count=0
        for i in range(0,diag_R[dl][2]):
            x=diag_L[dl][0]-i
            y=diag_L[dl][1]+i
            if board[y][x]==who:               
                count+=1
            else:
                count=0
            if count==4:
                return True
        count=0
    return(False) 
"""checks if the player has won in the 4 possible ways:
    horizontal, verticle, diagonally left & diagonally right.
    It does this by looping through each direction and adds 1 to a count for
    every counter (who) it passes, it will reset the count to zero if it 
    encounters a 0, opositions counter or end of the board.Returns True if 
    count==4 for 4 in a row, or else returns False""" 
def possibleWin(board,who):
    moves=getValidMoves(board)
    for x in range (0,7):
        for y in range(0,6):
            if (board[y][x]==1 or board[y][x]==2 or (y==5 and board[y][x]==0)) and x in moves:
                board2 = deepcopy(board)
                if y==5 and board[y][x]==0:
                    board2[y][x] = who
                else:
                    board2[y-1][x] = who      
                if hasWon(board2,who):
                    return int(x)
                else:
                    break    
    return "False"
"""Cycles through every possible move and then creates a copy of the board if
the player were to place a counter in that space, It then checks if that move
will result in a win using hasWon(), If so it will return that move, if not
it will return "False"(using boolean(False) clashed with int(0))"""
def suggestMove1(board,who):
    result1=possibleWin(board,who)
    if who==1:
        result2=possibleWin(board,2)
    else:
        result2=possibleWin(board,1)
    if result1 != "False":
        return result1
    elif result2 !="False":
        return result2
    else:
        return getValidMoves(board)[0]
"""This easy computer opponent will check if itself can win using possibleWin()
and return that move. If not then check if the opponent can win and return that
that move, If not return first available move"""
def scoreBoard(board,who):
    score=0
    for x in range (0,7):
        for y in range (0,6):
            if board[y][x]==who:
                """virtical win possible"""
                count=0                
                for j in range(y,max(y-4,0),-1):
                    if board[j][x]==who or board[j][x]==0:
                        count+=1
                if count==4:
                    score+=1
                """horizontal Right"""
                count=0
                for i in range(x,min(x+4,7)):
                    if board[y][i]==who or board[y][i]==0:
                        count+=1
                if count==4:
                    if y==5:
                        score+=2
                    score+=1
                """horizontal Left"""
                count=0
                for i in range(x,max(x-4,0),-1):
                    if board[y][i]==who or board[y][i]==0:
                        count+=1
                if count==4:
                    if y==5:
                        score+=2
                    score+=1
                """diagonal \ down"""
                count=0
                i=x
                j=y
                while (i!=7 and j!=6):
                    if board[j][i]==who or board[j][i]==0:
                            count+=1
                    i+=1
                    j+=1                            
                if count==4:
                    score+=1
                """diagonal \ up"""
                count=0
                i=x
                j=y
                while (i!=-1 and j!=-1):
                    if board[j][i]==who or board[j][i]==0:
                            count+=1
                    i-=1
                    j-=1
                if count==4:
                    score+=1
                """diagonal / up"""
                count=0
                i=x
                j=y
                while (i!=7 and j!=-1):
                    if board[j][i]==who or board[j][i]==0:
                            count+=1
                    i+=1
                    j-=1
                if count==4:
                    score+=1
                """diagonal /down"""
                count=0
                i=x
                j=y
                while (i!=-1 and j!=6):
                    if board[j][i]==who or board[j][i]==0:
                            count+=1
                    i-=1
                    j+=1
                if count==4:
                    score+=1 
    return score
"""This gives the board a score of how good the board is for the player. It
scores this by the number of possible ways there are to win (giving extra weight
to horizontal wins to give a more competative start)"""
def suggestMove2(board,who):    
    result1=possibleWin(board,who)
    if who==1:
        result2=possibleWin(board,2)
    else:
        result2=possibleWin(board,1)
    if result1 != "False" or result1==0:
        return result1
    elif result2 !="False" or result1==0:
        return result2
    else:    
        moves=getValidMoves(board)
        #best[score,position]
        best=[-200,0]
        for x in range (0,7):
            for y in range(0,6):
                if (board[y][x]==1 or board[y][x]==2 or (y==5 and board[y][x]==0)) and x in moves:
                    board2 = deepcopy(board)
                    if y==5 and board[y][x]==0:
                        board2[y][x] = who
                    else:
                        board2[y-1][x] = who  
                    if who==1:
                        score=scoreBoard(board2,1)-scoreBoard(board2,2)
                    else:
                        score=scoreBoard(board2,2)-scoreBoard(board2,1)
                    print("Column: "+str(x+1)+", score= "+str(scoreBoard(board2,2))+" - "+str(scoreBoard(board2,1))+ " = " +str(score) )
                    if score>best[0]:
                        best[0]=score
                        best[1]=x         
                    break
        return best[1]
"""This function creates a copy of a board for each possible move a player
could make and then scores it for both the player and the opposition. It then
subtracts the opposition score from the player score to give a score for the
move. The move with the highest score is returned"""
def loadGame(filename):
    if filename=="":
        filename="game"
    filename=(filename+".txt")
    try:
        file = open(filename, "r")
    except FileNotFoundError:
        raise FileNotFoundError("Game file not found")
    try:
        line = file.readlines()
        line = [x.strip() for x in line]
        try:
            player1=str(line[0])
            player2=str(line[1])
            who=int(line[2])
        except Exception:
            raise ValueError("Load file is not of the correct format")
        if (who!= 1 and who!=2):
            raise ValueError("Load file is not of the correct format")
        board=[[],[],[],[],[],[]]
        for i in range(3,9):
            s=line[i]
            s = s.replace(',', '')
            s=list(s)
            if len(s)!=7:
                raise ValueError("Load file is not of the correct format")
            for j in range(0,7):
                if s[j]!=1 or s[j]!=2 or s[j]!=0:
                    raise ValueError("Load file is not of the correct format")
                board[i-3].append(int(s[j]))   
            game = {
                    'player1' : player1,
                    'player2' : player2,
                    'who' : who,
                    'board' : board
                    }
    except ValueError:
        raise ValueError("Load file is not of the correct format")
    return game
"""This load function will load the file (filename or "game.txt") and read it by line. It reads the
first 3 lines for "player1", "player2" and "Who" checking that they have the
correct type and value and raising an exception otherwise.
It then reads the next 6 lines to and converts the strings into the correct
format for board in the game dictionary(also checking every number is 0,1 or 2
and that there are the correct number of entries)."""
def saveGame(game,filename):
    if filename=="":
        filename="game"
    filename=(filename+".txt")
    print("saved as: "+filename)
    file = open(filename, "w") 
    str1=(str(game["player1"])+"\n")
    str2=(str(game["player2"])+"\n")
    str3=(str(game["who"])+"\n")
    board=game["board"]
    str4=""
    for y in range (0,6):
        for x in range(0,7):
            if board[y][x]==1:
               str4=str4+"1"
            elif board[y][x]==2:
               str4=str4+"2"
            else:
                str4=str4+"0"
            if x!=6:
                str4=str4+","
            elif x==6:
                str4=str4+"\n"
    L = [str1, str2, str3, str4]
    file.writelines(L) 
    file.close()
"""Converts each section of the game dictionary into the required string format,
    a for loop is used to record the board. Each section is saved as a string
    and stored in a list then this is written to the file line by line."""    
# USE EXACTLY THE PROVIDED FUNCTION NAMES AND VARIABLES!
# ------------------- Main function --------------------
def play():
    print("*"*55)
    print("***"+" "*8+"WELCOME TO PYTHON CONNECT FOUR!"+" "*8+"***")
    print("*"*55,"\n")
    print("Enter the players' names, or type 'C' or 'L'.\n")
    player1=input("Player 1 name: ")
    player1=player1.capitalize()
    if player1=="L":
        filename=input("Enter the filename of saved game: ")
        game=loadGame(filename)
        player1=game["player1"]
        player2=game["player2"]
    else:
        player2=input("Plyer 2 name: ")    
        player2=player2.capitalize()
        game=newGame(player1,player2)
    board=game["board"]
    who=game["who"]
    printBoard(board)
    player=[player1,player2]
    counter=["O","X"]
    """If a game is being loaded (input "L") then load the game dictionary from
    the given file or else load a new game dictionary with the players names"""
    finish=False
    valid=False
    while (finish==False):
        if (player[who-1]=="C"):
            move=suggestMove2(board,who)                
            print("\nC ("+counter[who-1]+") has placed a piece in column "+str(move+1))
        else:
            while (valid==False):
                move=input(player[who-1]+ " ("+counter[who-1]+"), enter the column you want to place your piece (1-7): ")
                if (move=="S"):
                    try:
                        filename=input("Enter a filename for this save game: ")
                        saveGame(game,filename)
                        return
                    except Exception:
                        print("SAVE FAILED")
                        continue
                    break
                try:                
                    move=int(move)-1
                except Exception:
                    valid=False
                if (move in getValidMoves(board)):
                    valid=True
                else:
                    valid=False
                    print("INVALID MOVE, Please enter again")                 
        board=makeMove(board,move,who)
        printBoard(board)
        """If the player is C it will choose a move based on the suggestMove2
          function. If not it will ask the user for a move and check its validity.
          If the player wishes to save it will carry out the saveGame function"""
        if hasWon(board,who):
            finish=True        
            winner=who
        if len(getValidMoves(board))==0:
            winner="draw"
            finish=True
        if who==1:
            who=2
        elif who==2:
            who=1
        valid=False        
        game["player1"]=player1
        game["player2"]=player2
        game["who"]=who
        game["board"]=board
    if (winner=="draw"):
        print("*"*55)
        print(" "*10+"Well done "+player[0]+" and "+player[1]+", the game was a draw"+" "*8)
        print("*"*55,"\n")        
    else:
        print("*"*55)
        print("***"+" "*8+"Well done "+player[winner-1]+" YOU WON!"+" "*8+"***")
        print("*"*55,"\n")
    """checking for a condition to finish the game, either run out of valid
      moves or a player winning and printing the required message and changing
      the finish variable to true to end the while loop"""
# the following allows your module to be run as a program
if __name__ == '__main__' or __name__ == 'builtins':
    play()


    
def test():
    
    board2=[[0,2,1,2,2,1,2],
           [1,2,1,1,1,2,1],
           [2,1,2,2,2,1,1],
           [1,2,1,1,2,2,2],
           [2,1,2,2,1,1,1],
           [1,2,1,1,2,1,2]]
    
    board=[ [0,0,1,2,0,0,0],
            [0,0,1,1,0,0,0],
            [2,2,1,2,0,0,0],
            [1,2,2,1,0,0,0],
            [2,1,1,2,0,0,0],
            [1,2,1,2,1,0,0] ]
    
    game = {
        'player1' : "Sam",
        'player2' : "C",
        'who' : 1,
        'board' : [ [0,0,1,2,0,0,0],
                   [0,0,1,1,0,0,0],
                   [2,2,1,2,0,0,0],
                   [1,2,2,1,0,0,0],
                   [2,1,1,2,0,0,0],
                   [1,2,1,2,1,0,0] ]
        }
    printBoard(board)
    #print(getValidMoves(board))
    #printBoard(makeMove(board,6,1))
    #print(hasWon(board,1))
    #print(possibleWin(board2,2))
    #game=loadGame("game1")
    #board=game["board"]
    #printBoard(board)
    #print(game["player1"])
    #print(game["player2"])
    #print(game["who"])    
    saveGame(game)
    #print(scoreBoard(board,1))
    
#test()