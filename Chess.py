import itertools
import copy
import inspect
WHITE = "white"
BLACK = "black"
gameboard = None

def canSeeKing(kingpos,piecelist, overridegameboard = None):
    global gameboard
overridegameboard = overridegameboard or gameboard
for piece,position in piecelist:
    if piece.isValid(position,kingpos,piece.Color,overridegameboard):
        return True

def isCheck(overridegameboard = None):
    global gameboard
overridegameboard = overridegameboard or gameboard
king = King
kingDict = {}
pieceDict = {BLACK : [], WHITE : []}
for position,piece in overridegameboard.items():
    if type(piece) == king:
        kingDict[piece.Color] = position
        print(piece)
        pieceDict[piece.Color].append((piece,position))
    if canSeeKing(kingDict[WHITE],pieceDict[BLACK], overridegameboard):
        return WHITE
    if canSeeKing(kingDict[BLACK],pieceDict[WHITE], overridegameboard):
        return BLACK
        return False

class Game:
    def init(self):
        global gameboard
        self.playersturn = WHITE
        self.message = "Input Your Move"
        gameboard = self.gameboard = {}
        self.placePieces()
        print("Chess program. Enter moves in algebraic notation separated by space. Example: a2-a4")
        self.main()

def placePieces(self):

    for i in range(0,8):
        self.gameboard[(i,1)] = Pawn(WHITE,uniDict[WHITE][Pawn],1)
        self.gameboard[(i,6)] = Pawn(BLACK,uniDict[BLACK][Pawn],-1)
        
    placers = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
    
    for i in range(0,8):
        self.gameboard[(i,0)] = placers[i](WHITE,uniDict[WHITE][placers[i]])
        self.gameboard[((7-i),7)] = placers[i](BLACK,uniDict[BLACK][placers[i]])
    placers.reverse()

    
def main(self):
    
    while True:
        self.printBoard()
        print(self.message)
        self.message = ""
        startpos,endpos = self.parseInput()
        try:
            target = self.gameboard[startpos]
        except:
            self.message = "could not find piece; index probably out of range"
            target = None
            
        if target:
            print("found "+str(target))
            if target.Color != self.playersturn:
                self.message = "This is Not Your Turn"
                continue
            if target.isValid(startpos,endpos,target.Color,self.gameboard):
                hasLegalMoves = False
                for position in self.gameboard:
                    piece = self.gameboard[position]
                    if (piece.Color == self.playersturn):
                        for move in piece.availableMoves(position[0], position[1], self.gameboard):
                            overridegameboard = copy.deepcopy(self.gameboard)
                            overridegameboard[move] = self.gameboard[position]
                            del overridegameboard[position]
                            if (isCheck(overridegameboard) != self.playersturn):
                                hasLegalMoves = True
                                break
                if (not hasLegalMoves):
                    if (isCheck() == self.playersturn) : print("You are in checkmate. " + ({WHITE: BLACK, BLACK: WHITE})[self.playersturn] + " wins!")
                    else : print("Stalemate. Nobody wins!")
                    return
                overridegameboard = copy.deepcopy(self.gameboard)
                overridegameboard[endpos] = self.gameboard[startpos]
                del overridegameboard[startpos]
                if (isCheck(overridegameboard) == self.playersturn) : self.message = "You are not allowed to put yourself in check!"
                else:
                    self.message = "That Move is Allowed"
                    self.gameboard[endpos] = self.gameboard[startpos]
                    del self.gameboard[startpos]
                    Check = isCheck()
                    if (Check):
                        self.message = "Player is in check"
                    if self.playersturn == BLACK:
                        self.playersturn = WHITE
                    else : self.playersturn = BLACK
            else : 
                self.message = "invalid move" + str(target.availableMoves(startpos[0],startpos[1],self.gameboard))
                print(target.availableMoves(startpos[0],startpos[1],self.gameboard))
        else : self.message = "There is no Piece in That Space"
            
def parseInput(self):
    try:
        a,b = input().split('-')
        a = ((ord(a[0])-97), int(a[1])-1)
        b = (ord(b[0])-97, int(b[1])-1)
        print(a,b)
        return (a,b)
    except:
        print("error decoding input. please try again")
        return((-1,-1),(-1,-1))
    
def printBoard(self):
    print("  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")
    for i in range(0,8):
        print("-"*32)
        print(chr(i+97),end="|")
        for j in range(0,8):
            item = self.gameboard.get((i,j)," ")
            print(str(item)+' |', end = " ")
        print()
    print("-"*32)

class Piece:
    def __init__(self,color,name):
        self.name = name
        self.position = None
        self.Color = color

    def isValid(self,startpos,endpos,Color,gameboard):
        if endpos in self.availableMoves(startpos[0],startpos[1],gameboard,Color):
            return True
            return False

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def availableMoves(self,x,y,gameboard,Color=None):
        print("ERROR: no movement for base class")

    def AdNauseum(self,x,y,gameboard, Color, intervals):
        answers = []
        for xint,yint in intervals:
            xtemp,ytemp = x+xint,y+yint
        while self.noConflict(gameboard, Color, xtemp, ytemp):
            #print(str((xtemp,ytemp))+"is in bounds")
            
            target = gameboard.get((xtemp,ytemp),None)
            if target is None: answers.append((xtemp,ytemp))
            elif target.Color != Color: 
                answers.append((xtemp,ytemp))
                break
            else:
                break
            
            xtemp,ytemp = xtemp + xint,ytemp + yint
    return answers
            
def isInBounds(self,x,y):
    "Checks if a position is on the board"
    if x >= 0 and x < 8 and y >= 0 and y < 8:
        return True
    return False

def noConflict(self,gameboard,initialColor,x,y):
    "Checks if a single position poses no conflict to the rules of chess"
    if self.isInBounds(x,y) and (((x,y) not in gameboard) or gameboard[(x,y)].Color != initialColor) : return True
    return False
chessCardinals = [(1,0),(0,1),(-1,0),(0,-1)]
chessDiagonals = [(1,1),(-1,1),(1,-1),(-1,-1)]

def knightList(x,y,int1,int2):
    return [(x+int1,y+int2),(x-int1,y+int2),(x+int1,y-int2),(x-int1,y-int2),(x+int2,y+int1),(x-int2,y+int1),(x+int2,y-int1),(x-int2,y-int1)]
def kingList(x,y):
    return [(x+1,y),(x+1,y+1),(x+1,y-1),(x,y+1),(x,y-1),(x-1,y),(x-1,y+1),(x-1,y-1)]

class Knight(Piece):
    def availableMoves(self,x,y,gameboard, Color = None):
        if Color is None : Color = self.Color
        return [(xx,yy) for xx,yy in knightList(x,y,2,1) if self.noConflict(gameboard, Color, xx, yy)]

class Rook(Piece):
    def availableMoves(self,x,y,gameboard ,Color = None):
        if Color is None : Color = self.Color
        return self.AdNauseum(x, y, gameboard, Color, chessCardinals)

class Bishop(Piece):
    def availableMoves(self,x,y,gameboard, Color = None):
        if Color is None : Color = self.Color
        return self.AdNauseum(x, y, gameboard, Color, chessDiagonals)

class Queen(Piece):
    def availableMoves(self,x,y,gameboard, Color = None):
        if Color is None : Color = self.Color
        return self.AdNauseum(x, y, gameboard, Color, chessCardinals+chessDiagonals)

class King(Piece):
    def availableMoves(self,x,y,gameboard, Color = None):
        if Color is None : Color = self.Color
        return [(xx,yy) for xx,yy in kingList(x,y) if self.noConflict(gameboard, Color, xx, yy)]

class Pawn(Piece):
    def init(self,color,name,direction):
        self.name = name
        self.Color = color
        self.direction = direction
def availableMoves(self,x,y,gameboard, Color = None):
    if Color is None : Color = self.Color
    answers = []
if (x+1,y+self.direction) in gameboard and self.noConflict(gameboard, Color, x+1, y+self.direction) : answers.append((x+1,y+self.direction))
if (x-1,y+self.direction) in gameboard and self.noConflict(gameboard, Color, x-1, y+self.direction) : answers.append((x-1,y+self.direction))
if (x,y+self.direction) not in gameboard and Color == self.Color and self.noConflict(gameboard, Color, x, y+self.direction) : answers.append((x,y+self.direction))# the condition after the and is to make sure the non-0capturing movement is not used in the calculation of checkmate
if (x,y+self.direction2) not in gameboard and Color == self.Color and self.noConflict(gameboard, Color, x, y+self.direction2) : answers.append((x,y+self.direction*2))# the condition after the and is to make sure the non-0capturing movement is not used in the calculation of checkmate
return answers

uniDict = {WHITE : {Pawn : "♙", Rook : "♖", Knight : "♘", Bishop : "♗", King : "♔", Queen : "♕" }, BLACK : {Pawn : "chess_pawn", Rook : "♜", Knight : "♞", Bishop : "♝", King : "♚", Queen : "♛" }}

if (name == "main"):
    input("Press the Enter Key to Exit")

Game()
