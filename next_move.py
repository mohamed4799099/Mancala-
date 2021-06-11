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