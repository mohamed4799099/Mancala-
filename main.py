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
          
            if(turn==0):
                if game_ended(board):
                   break
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
                 if game_ended(board):
                    break
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
        
           
            if(turn==0):
                if game_ended(board):
                   break
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
                 if game_ended(board):
                         break
                 while (True):
                   
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
        
