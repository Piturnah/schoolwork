import random
import csv
import os
import multilines as auto

totalIn = 0
totalOut = 0

def game(tokens, toHold, output):
    global totalIn
    global totalOut
    
    cards = {
        1 : "7",
        2 : "BAR",
        3 : "Bell",
        4 : "Cherry",
        5 : "MELON",
        6 : "GRAPES",
        7 : "HORSE"
        }
    
    input("You have "+ str(tokens) +" valid tokens remaining.\nPress enter to start the game.")
    
    if tokens > 0:
        for i in range (3):
            try:
                if not toHold[i]:
                    output[i] = cards[random.randint(1,7)]
            except:
                try:
                    output.append(cards[random.randint(1,7)])
                except:
                    output = []
                    output.append(cards[random.randint(1,7)])

        print("\n" + auto.row(output, 13))

        hands = {
                "7" : 20,
                "BAR" : 5,
                "Bell" : 3,
                "Cherry" : 1
                }

        #opens previous-turns.txt for appending
        out = open("previous-turns.txt", "a")
        out.write("\n"+str(output))
        
        if output[0] == output[1] == output[2] and output[0] in hands:
            
            print(auto.row("Congratulations! You won £" + str(hands[output[0]]), 0))
            tokens += hands[output[0]] * 10

            out.write("\nDISPENSED £"+ str(hands[output[0]]))
            totalOut += hands[output[0]]
        out.close()
        
        userIn = ""
        while userIn != "1":
            userIn = input("""1. Continue
2. Hold an item
3. Add funds
4. Read files
5. Quit

> """)
            if userIn == "2":
                if toHold.count(True) < 2:
                    holdIndex = hold_item(output)
                    #toggles the bool value of the specified band
                    toHold[holdIndex] = not toHold[holdIndex]
                else:
                    print("You are already holding two items!")
                    
            elif userIn == "3":
                game(receive_money() + tokens, toHold, output)
                
            elif userIn == "4":
                read_files()
                
            elif userIn == "5":
                turnID = 0
                with open("money-in-out.csv") as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    readCSV = list(readCSV)
                    turnID = str(int(readCSV[-1][0]) + 1)
                
                moneyCSV = open("money-in-out.csv", "a")
                moneyCSV.write("\n" + turnID + "," + str(totalIn) + "," + str(totalOut))
                moneyCSV.close()
                
                quit()
            elif userIn != "1":
                print("invalid input.")

        if tokens <= 1:
            input("""You have no remaining tokens. Press Enter.""")
            game(receive_money(), toHold, output)
        else:
            game(tokens -1, toHold, output)
            
        output = []

#returns integer representing index of band to be toggled
def hold_item(bands):
    validIn = False
    while not validIn:
        userIn = input("Which bar would you like to hold (1, 2, or 3)?\n\n> ")
        if userIn == "1":
            return 0
            validIn = True
        elif userIn == "2":
            return 1
            validIn = True
        elif userIn == "3":
            return 2
            validIn = True
        else:
            validIn = False

def read_files():
    userIn = input("""What would you like to read?
1. Money I/O
2. Previous Turns

> """)

    valid = False
    while not valid:
        if userIn == "1":
            with open("money-in-out.csv") as csvfile:
                readCSV = list(csv.reader(csvfile, delimiter = ","))
                userIn = int(input("Enter the index of the iteration you wish to view I/O for."))
            
                print("In: £" + readCSV[userIn][1] + "\nOut: £" + readCSV[userIn][2])
                
        elif userIn == "2":
            os.system("open " + "previous-turns.txt")
            valid = True

        input("\n> ")
        return

#subroutine to receive money, returns value of additional plays
def receive_money():
    global totalIn
    
    valid = False
    #receive money input with value error exception and
    #checking if value divisible by 10
    while not valid:
        try:
            tokensIn = int(input("Please enter money in pence. 10p per play.\n\n> "))
            if tokensIn <=0:
                print("Please enter a valid amount.")
            elif tokensIn % 10 != 0:
                print("Amount must be divisible by 10.")
            else:
                valid = True
                totalIn += tokensIn // 100
                return tokensIn // 10
        except ValueError:
            print("Please enter a valid amount.")

def menu():
    input(auto.box("""
 SLOT MACHINE

 Winning hands:
 7 7 7 - £20.00
 BAR BAR BAR - £5.00
 Bell Bell Bell - £3.00
 Cherry Cherry Cherry - £1.00

 Press enter to play.

""", 40) + "\n\n> ")

    #starts the first round with initial parameters
    game(receive_money(), [False, False, False], [])

menu()
