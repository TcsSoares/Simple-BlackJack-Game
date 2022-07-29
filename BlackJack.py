# Imports
from random import shuffle
from os import system

# Main Game Loop
while(True):
        packCards = [] # Playing Cards.
        my,dealer = [],[] # Cards of Each Player.
        dealerScore = myScore = 0 # Score of Each Player.
        suit,num = ["\u2665","\u2660","\u2666","\u2663"],["A","2","3","4","5","6","7","8","9","10","J","Q","K"] # Cards Attribute

        # Cards Generator
        for i in range (len(num)):
                for j in range (len(suit)):
                        packCards.append(num[i] + suit[j])
                shuffle(packCards)

        # Score Counter
        def score(player):
                score = 0
                for i in range (len(player)):
                        if(player[i][0] == "J" or player[i][0] == "Q" or player[i][0] == "K" or player[i][0] == "1"):
                                score += 10
                        elif(player[i][0] == "A"):
                                score += 11
                        else:
                                score += int(player[i][0])
                for card in player:
                        if(card[0] == "A" and score > 21):
                                score -= 10
                return score

        # Starting Hand Generator
        for i in range (2):
                my.append(packCards[0]) , packCards.pop(0)
                dealer.append(packCards[0]) , packCards.pop(0)

                myScore = score(my)
                dealerScore = score(dealer)

        # Starting Hand Announcement
        system('cls')
        print("Your Cards:  %s  %s" %(my[0],my[1]))
        print("Your Score: %s" %myScore)
        print("\nDealer's Cards:  %s   **" %dealer[0])
        if(myScore == 21):
                print("\nYou Got a BlackJack !")
                myScore="BlackJack"
        elif(dealerScore == 21):
                print("\nThe Dealer Got a BlackJack !")
                dealerScore="BlackJack"
        
        # Player Turn Loop
        while(myScore != "BlackJack" and dealerScore != "BlackJack"):
                if(myScore <= 21 and dealerScore <= 21):
                        case=input("\nInsert:\n ( c ) to Pick up a Card.\n ( p ) to Stop.\n ( s ) to Exit.\n")
                        if(case == "c"):
                                system('cls')
                                my.append(packCards[0]) , packCards.pop(0)
                                myScore = score(my)
                        elif(case == "p"):
                                system('cls')
                                print("You Stop With: %s " %myScore)
                                break
                        elif(case == "s"):
                                exit()
                        system('cls')
                        print("Your Cards:  ",end="")
                        for i in range(len(my)):
                                print(my[i],end="  ")
                        print("\nYour Score: %s" %myScore)
                        print("\nDealer's Cards:  %s   **" %dealer[0])
                else:
                        break
        
        # Dealer's Turn Announcement
        if(myScore != "BlackJack" and dealerScore != "BlackJack"):
                if(myScore <= 21):
                        print("\nDealer's Turn !")
                        print("\nDealer Cards: %s e %s" %(dealer[0],dealer[1]))

        # Dealer's Turn Loop
        while(myScore != "BlackJack" and dealerScore != "BlackJack"):
                if(myScore <= 21 and dealerScore <= 21):
                        if((((dealerScore > myScore or dealerScore == myScore) and dealerScore > 11) or dealerScore >= 18) and dealerScore <= 21):
                                print("\nThe Dealer Stop !")
                                break
                        else:
                                print("\nThe Dealer Pick up a Card !")
                                dealer.append(packCards[0]) , packCards.pop(0)
                                dealerScore = score(dealer)
                                print("Dealer's Cards:  ",end="")
                                for i in range (len(dealer)):
                                        print(dealer[i],end="  ")
                                print()
                else:
                        break

        # End Game Conditional
        if(myScore != "BlackJack" and dealerScore != "BlackJack"):
                input("\n\n( continue... )")
                system('cls')
                print("Dealer's Score: %s.\nYour Score: %s" %(dealerScore,myScore))
                if((dealerScore > myScore and dealerScore <= 21) or (myScore > 21)):
                        print("\nDealer Wins !")
                elif((myScore > dealerScore or dealerScore > 21) and myScore <= 21):
                        print("\nYou Win !")
                elif(myScore == dealerScore):
                        print("\nDraw !")

        # Input to Hold the Loop
        input("\n\n( Press any Key to Play Again... )")