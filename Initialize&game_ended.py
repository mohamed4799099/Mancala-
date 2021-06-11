board=[]
def Initialize_Board(board):
    for i in range(14):
        board.append(0)
    for i in range(6):
        board[i]=4
        
    for i in range(7,13):
        board[i]=4    
    return board

def game_ended(board):
    flag1=False
    flag2=False
    flag=True ####### returned_flag
    sum1=0
    sum2=0
    for i in range(6):
        sum1=sum1+board[i]
        if i==5 and sum1==0:
            flag1=True
    for i in range(7,13):
        sum2=sum2+board[i]
        if i==12 and sum2==0:
            flag2=True
            
            
    if (flag1==True or flag2==True) :
        return flag
    
    else :
        return not flag
