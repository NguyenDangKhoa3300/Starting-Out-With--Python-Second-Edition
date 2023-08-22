def main():
    infoWrite()
    infoRead()

def infoWrite():
    try:
        file_handler = open('golf.txt', 'w')
        file_handler.write('PLAYER NAME' + '\t' + 'SCORES' + '\n' + '---------------------------' + '\n')

        player_name = input('Enter a player name: ')
        player_score = input('Enter a player score: ')

        while player_name != '' or player_score != '':
            file_handler.write(player_name + '\t\t' + player_score + '\n')
            #file_handler.write(player_score + '\n')

            player_name = input('Enter a player name: ')
            player_score = input('Enter a player score: ')
        
        file_handler.close()
    
    except:
        print('Something wrong occurs!')

def infoRead():
    try:
        file_handler = open('golf.txt', 'r')

        for lines in file_handler:
            print(lines.rstrip('\n'))
        
        file_handler.close()

    except:
        print('Something wrong occurs!')
    
main()