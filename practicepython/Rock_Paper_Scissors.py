#Rock Paper Scissors

print('''Please pick one:
            rock
            scissors
            paper''')

#get userinput in proper format
game_dict = {'rock': 1, 'paper': 2, 'scissors': 3}
def correctInput(string,dict,message):
    returnValue=dict.get(string)
    if returnValue is None:
        print("Incorrect Input.Select again")
        string= str(input(message))
        returnValue=correctInput(string,dict,message)
    return returnValue


while True:
    #user input in correct format
    player_a = str(input("Player a: "))
    a = correctInput(player_a,game_dict,"Player a: ")
    player_b = str(input("Player b: "))
    b = correctInput(player_b,game_dict,"Player b: ")
    dif = a - b
    if dif in [1, -2]:
        print('player a wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    elif dif in [2, -1]:
        print('player b wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    else:
        print('Draw.Please continue.')
        print('')
