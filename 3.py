print('''Welcome to Treasure Island.\nYour mission is to find the treasure.''')
a=input('''You're at a cross road. Where do you want to go?\n\tType'Left' or 'Right' \n''')
if(a=='right'):
    print("You fell into a hole. Game Over.")
    
else:
    print("You've come to a lake. There is an island in the middle of the lake.")
    b=input('''Type "wait" to wait for a boat. Type "swim" to swim across.\n''')
    if(b=="swim"):
        print('''You get attacked by an angry trout. Game Over.''')
    else:
        print('''You arrive at the island unharmed. There is a house with 3 doors.''')
        c=input('''One red, one yellow and one blue. Which colour do you choose?\n''')
        if(c=='red'):
            print('''It's a room full of fire. Game Over.''')
        elif(c=='yellow'):
            print('''You found the treasure! You Win!''')
        else:
            print('''You enter a room of beasts. Game Over.''')