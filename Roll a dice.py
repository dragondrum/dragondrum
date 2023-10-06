import random

running = True

while running == True:

    dice_choice = input("Choose the number of sides of your dice: ")

    try: 

        random_number = random.randint(1,int(dice_choice))
        print('Rolled a',random_number,"\n")

    except:

        if dice_choice == 'exit':
            running = False

        elif dice_choice == 'help':
            print("Sorry buddy, help hasn\'t been implemented yet... Come back later...\n")
            running = True
        
        elif dice_choice == 'restart':
            print("")
            running = True

        elif dice_choice == 'commands':
            print("Implemented commands : help, exit, restart, commands\n")
            running = True

        else:
            print(dice_choice,"is not a valid integer\n")