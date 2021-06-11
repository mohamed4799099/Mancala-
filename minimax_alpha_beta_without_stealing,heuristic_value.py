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
    
    
    
    
def heuristic_value(board):
      
        return board[13]-board[6]    

