board=[]
def Initialize_Board(board):
    for i in range(14):
        board.append(0)
    for i in range(6):
        board[i]=4
        
    for i in range(7,13):
        board[i]=4    
    return board

def next_move_without_stealing(inputt,board):
    flag=False ######## 3shan lw 7at a5er stone f l mancala bt3to y-turn tani
    temp_stones=board[inputt] ### 3shan a-store 3add l stones ely fe l cup ely a5tarha 
    board[inputt]=0 ###### 3shan ana ba5od kol ely f l cup

    if inputt>6: ############## moves for computer
        while(temp_stones>0):
            inputt=inputt+1 ###### a5osh f l cup ely ba3dya
            if(inputt==14):
                inputt=0 ######## 3shan lw d5l f cups l player
            ####### lw d5l f cupes l player my5oshsh f l mancala bt3to
            if inputt==6:
                continue    
            board[inputt]=board[inputt]+1 
            temp_stones=temp_stones-1
            
        if inputt==13: ########### y3ni lw l last step kant f l mancala bt3to lazm y5od turn kman
            flag=True 
            
       
    
        
    else : ###### moves for player 
        while(temp_stones>0):
            inputt=inputt+1 ###### a5osh f l cup ely ba3dya
            if(inputt==14):
                inputt=0 ######## 3shan lw d5l f cups l player
            ####### lw d5l f cupes l player my5oshsh f l mancala bt3to
            if inputt==13:
                continue    
            board[inputt]=board[inputt]+1 
            temp_stones=temp_stones-1
            
        if inputt==6: ########### y3ni l last step kant f l mancala bt3to lazm y5od turn kman
            flag=True 
            
       
            
            
            
    return flag ######## 3shan lw b true w kant a5r step f l mancala a-call l fn de tani
#############################################################


def next_move(inputt,board):
    flag=False ######## 3shan lw 7at a5er stone f l mancala bt3to y-turn tani
    temp_stones=board[inputt] ### 3shan a-store 3add l stones ely fe l cup ely a5tarha 
    board[inputt]=0 ###### 3shan ana ba5od kol ely f l cup

    if inputt>6: ############## moves for computer
        while(temp_stones>0):
            inputt=inputt+1 ###### a5osh f l cup ely ba3dya
            if(inputt==14):
                inputt=0 ######## 3shan lw d5l f cups l player
            ####### lw d5l f cupes l player my5oshsh f l mancala bt3to
            if inputt==6:
                continue    
            board[inputt]=board[inputt]+1 
            temp_stones=temp_stones-1
            
        if inputt==13: ########### y3ni lw l last step kant f l mancala bt3to lazm y5od turn kman
            flag=True 
            
        if  inputt>6 and inputt != 13 and  board[inputt]==1 : ###### lw hwa lsa f l cups bt3to w md5lsh f l cups bta3t l player w kan last step f empty cup lazm yd5lha l mancala bt3to w y5od kol l stones ely f l opposite cup
            board[13]=board[13]+board[-inputt+12] ###### yzwd l mancala b stones ely f l opposite cup
            board[inputt]=0
            board[-inputt+12]=0 ##### -inputt+12 de equation trbot kol cup b l opposite cup
            
            
            
            
            
            
        
        
        
        
    else : ###### moves for player 
        while(temp_stones>0):
            inputt=inputt+1 ###### a5osh f l cup ely ba3dya
            if(inputt==14):
                inputt=0 ######## 3shan lw d5l f cups l player
            ####### lw d5l f cupes l player my5oshsh f l mancala bt3to
            if inputt==13:
                continue    
            board[inputt]=board[inputt]+1 
            temp_stones=temp_stones-1
            
        if inputt==6: ########### y3ni l last step kant f l mancala bt3to lazm y5od turn kman
            flag=True 
            
        if  inputt<6 and board[inputt]==1 : ###### lw hwa lsa f l cups bt3to w md5lsh f l cups bta3t l player w kan last step f empty cup lazm yd5lha l mancala bt3to w y5od kol l stones ely f l opposite cup
            board[6]=board[6]+board[-inputt+12] ###### yzwd l mancala b stones ely f l opposite cup
            board[inputt]=0
            board[-inputt+12]=0 ##### -inputt+12 de equation trbot kol cup b l opposite cup
            
            
            
    return flag ######## 3shan lw b true w kant a5r step f l mancala a-call l fn de tani  





#################################################################################
#################################################################################
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
            
        
            
def The_winner(board):
    sum_computer=0
    sum_player=0
    if game_ended(board):
        for i in range(0,7):
             sum_player=sum_player+board[i]
        for i in range(7,14):     
              sum_computer=sum_computer+board[i]
        
    if sum_player>sum_computer:
        return "the winner is player with number of stones = " + str(sum_player)
    else :
        return "the winner is computer with number of stones = " + str(sum_computer)
    
    
    
def heuristic_value(board):
      
        return board[13]-board[6]
            
    
    
 
def minimax_alpha_beta(board, depth, alpha, beta , Maxmizer):
    
    if depth == 0 or game_ended(board):
            return heuristic_value(board),-1 ######### -1 3shan l fn btrg3 two arguments
    if Maxmizer: ##### maximizer
        alpha1 = -100000000  ##### value to indicate it's infinite
        the_move = -1 ###### to empty the variable move
        for i in range(7,13):
            if board[i]==0: ############# lw l cup fadya 5alac malhash lazma l cup de 
                continue 
            temp_board=board[:]
            maxmizer =next_move(i,temp_board)
            alpha_new,b = minimax_alpha_beta(temp_board, depth-1, alpha, beta, maxmizer)
            if alpha1< alpha_new:
                    the_move=i
                    alpha1 =alpha_new
                    alpha = max(alpha1, alpha)
            if alpha >= beta :
                 break
        return alpha1, the_move
    else:########### minimizer
        beta1 = 100000000
        the_move = -1
        for i in range(0,6):   
            if board[i]==0: ############# lw l cup fadya 5alac malhash lazma l cup de 
                    continue 
            temp_board=board[:]
            maxmizer =next_move(i,temp_board)
            beta_new,b= minimax_alpha_beta(temp_board, depth-1, alpha, beta,not maxmizer) ###### not maxmixer 3shan a5leha b false w a5osh l else (code l minimizer)
            if beta_new < beta1:
                the_move=i
                beta1 =beta_new
                beta=min(beta,beta1)
            if alpha >= beta :
                     break
        return beta1, the_move
################################################################
def minimax_alpha_beta_without_stealing(board, depth, alpha, beta , Maxmizer):
    
    if depth == 0 or game_ended(board):
            return heuristic_value(board),-1 ######### -1 3shan l fn btrg3 two arguments
    if Maxmizer: ##### maximizer
        alpha1 = -100000000  ##### value to indicate it's infinite
        the_move = -1 ###### to empty the variable move
        for i in range(7,13):
            if board[i]==0: ############# lw l cup fadya 5alac malhash lazma l cup de 
                continue 
            temp_board=board[:]
            maxmizer =next_move_without_stealing(i,temp_board)
            alpha_new,b = minimax_alpha_beta_without_stealing(temp_board, depth-1, alpha, beta, maxmizer)
            if alpha1< alpha_new:
                    the_move=i
                    alpha1 =alpha_new
                    alpha = max(alpha1, alpha)
            if alpha >= beta :
                 break
        return alpha1, the_move
    else:########### minimizer
        beta1 = 100000000
        the_move = -1
        for i in range(0,6):   
            if board[i]==0: ############# lw l cup fadya 5alac malhash lazma l cup de 
                    continue 
            temp_board=board[:]
            maxmizer =next_move_without_stealing(i,temp_board)
            beta_new,b= minimax_alpha_beta_without_stealing(temp_board, depth-1, alpha, beta,not maxmizer) ###### not maxmixer 3shan a5leha b false w a5osh l else (code l minimizer)
            if beta_new < beta1:
                the_move=i
                beta1 =beta_new
                beta=min(beta,beta1)
            if alpha >= beta :
                     break
        return beta1, the_move          
    

if __name__ == "__main__":
    temp_board=[]
    board=Initialize_Board(board)
    print(board)
    print("please add the depth : ")
    depth= int(input())
    print("please add 0 if you want it in stealing mode or add 1 if you want it in non-stealing mode :")
    mode=int(input())
    print("choose if you want to start the game ,please insert 1 if you want to start and 0 if you want to take second turn :")
    turn=int(input())

    
    
    if(mode==0):
        while(True):
            if game_ended(board):
                break
            if(turn==0):
                while(True):
                    print("The Turn of AI")
                    t,the_bestmove =  minimax_alpha_beta(board,depth,-1000000,1000000,True) ######## dh kda hydek a7san le3ba t5le l ai yeksb
                    flag_replay=next_move(the_bestmove,board) ####### flag 3shan yshof 5ad le3ba tanya wla l2a
                    print(board)
                    if (not flag_replay) or game_ended(board) :
                      break
        
                while (True):
                    if game_ended(board):
                         break
                    print("play") 
                    inputt_from_player= int(input())
                    if (inputt_from_player>5 or inputt_from_player<0):
                        print("please put true number related to your cups")
                        continue
                        
                    if (board[inputt_from_player]==0):
                        print("this an empty cup , please choose another play ")
                        continue
        
                    flag_replay2=next_move(inputt_from_player,board)
                    print(board)
                    if (not flag_replay2) or game_ended(board) :
                        break
                    
                    
            else:
                 while (True):
                    if game_ended(board):
                         break
                    print(board) 
                    print("play") 
                    inputt_from_player= int(input())
                    if (inputt_from_player>5 or inputt_from_player<0):
                        print("please put true number related to your cups")
                        continue
                        
                    if (board[inputt_from_player]==0):
                        print("this an empty cup , please choose another play ")
                        continue
        
                    flag_replay2=next_move(inputt_from_player,board)
                    print(board)
                    if (not flag_replay2) or game_ended(board) :
                        break
                    
                 while(True):
                    print("The Turn of AI")
                    t,the_bestmove =  minimax_alpha_beta(board,depth,-1000000,1000000,True) ######## dh kda hydek a7san le3ba t5le l ai yeksb
                    flag_replay=next_move(the_bestmove,board) ####### flag 3shan yshof 5ad le3ba tanya wla l2a
                    print(board)
                    if (not flag_replay) or game_ended(board) :
                      break    
                    
                    
                
                
        print("the Game is end and : ",The_winner(board))
        print(board)
    else:
        while(True):
            if game_ended(board):
                break
            if(turn==0):
                while(True):
                    print("The Turn of AI")
                    t,the_bestmove =  minimax_alpha_beta_without_stealing(board,depth,-1000000,1000000,True) ######## dh kda hydek a7san le3ba t5le l ai yeksb
                    flag_replay=next_move_without_stealing(the_bestmove,board) ####### flag 3shan yshof 5ad le3ba tanya wla l2a
                    print(board)
                    if (not flag_replay) or game_ended(board) :
                      break
        
                while (True):
                    if game_ended(board):
                         break
                    print("play") 
                    inputt_from_player= int(input())
                    if (inputt_from_player>5 or inputt_from_player<0):
                        print("please put true number related to your cups")
                        continue
                        
                    if (board[inputt_from_player]==0):
                        print("this an empty cup , please choose another play ")
                        continue
        
                    flag_replay2=next_move_without_stealing(inputt_from_player,board)
                    print(board)
                    if (not flag_replay2) or game_ended(board) :
                        break
                    
                    
            else:
                 while (True):
                    if game_ended(board):
                         break
                    print(board) 
                    print("play") 
                    inputt_from_player= int(input())
                    if (inputt_from_player>5 or inputt_from_player<0):
                        print("please put true number related to your cups")
                        continue
                        
                    if (board[inputt_from_player]==0):
                        print("this an empty cup , please choose another play ")
                        continue
        
                    flag_replay2=next_move_without_stealing(inputt_from_player,board)
                    print(board)
                    if (not flag_replay2) or game_ended(board) :
                        break
                    
                 while(True):
                    print("The Turn of AI")
                    t,the_bestmove =  minimax_alpha_beta_without_stealing(board,depth,-1000000,1000000,True) ######## dh kda hydek a7san le3ba t5le l ai yeksb
                    flag_replay=next_move_without_stealing(the_bestmove,board) ####### flag 3shan yshof 5ad le3ba tanya wla l2a
                    print(board)
                    if (not flag_replay) or game_ended(board) :
                      break    
                    
                    
                
                
        print("the Game is end and : ",The_winner(board))
        print(board)
        dummy=int(input())
        
       


    
    
    
