board={'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '}
def print_board(board):
    print(board['1']+'|'+ board['2']+'|'+board['3'] )
    print('--------------')
    print(board['4']+'|'+board['5']+'|'+board['6'] )
    print('--------------')
    print(board['7']+'|'+board['8']+'|'+board['9'] )

player="x"
for i in range(0,10):
    user=input("Enter a number: ")
    if(board[user] == ' '):
        board[user]=player


        
        if(board['1'] == board['2'] == board['3'] and board['1'] != " " or 
        board['4'] == board['5'] == board['6'] and board['4'] != " "
        or board['7'] == board['8'] == board['9'] and board['7'] != " " 
        or board['1'] == board['4'] == board['7'] and board['7'] != " "or
        board['2'] == board['5'] == board['8'] and board['2'] != " "  or
        board['3'] == board['6'] == board['9'] and board['3'] != " " or 
        board['1'] == board['5'] == board['9'] and board['1'] != " " or
        board['3'] == board['5'] == board['7']and board['7'] != " "):
                   print_board(board)
                   print("Player"+player+"is the winner")
                   break
        if(player=="x"):
           player="o"
        else:
            player="x"
    else:
        print("Already present.Select another location")
        i=i-1




        print_board(board)