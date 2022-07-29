# Imports
from random import shuffle
from os import system

system('cls')

#Language Select
while(True):
        print("Choose Your Language: \n")
        print("Insert ( 1 ) to select English ( not revised )\nInsert ( 2 ) to select Portuguese")
        language = input()
        if(language == "1" or language == "2"):
                break
        else:
                system('cls')
                print("Error: Invalid Arguments")
                input("\n( Continue... )")
                system('cls')

# Main Game Loop
while(True):

        #Variables
        packCards = [] # Playing Cards.
        my,dealer = [],[] # Cards of Each Player.
        dealerScore = myScore = 0 # Score of Each Player.
        suits,values = ["\u2665","\u2660","\u2666","\u2663"],["A","2","3","4","5","6","7","8","9","10","J","Q","K"] # Cards Attribute

        # Cards Generator
        for value in values:
                for suit in suits:
                        packCards.append(value + suit)
                shuffle(packCards)

        # Score Counter
        def score(player):
                score = 0
                for card in player:
                        if(card[0] == "J" or card[0] == "Q" or card[0] == "K" or card[0] == "1"):
                                score += 10
                        elif(card[0] == "A"):
                                score += 11
                        else:
                                score += int(card[0])
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
        if(language == "1"):
                print("Your Cards:  %s  %s" %(my[0],my[1]))
                print("Your Score: %s" %myScore)
                print("\nDealer's Cards:  %s   **" %dealer[0])
        elif(language == "2"):
                print("Suas Cartas Iniciais São:  %s  %s" %(my[0],my[1]))
                print("Você Possui %s Pontos" %myScore)
                print("\nCartas Do Dealer:  %s  **" %dealer[0])
        if(myScore == 21):
                if(language == "1"):
                        print("\nYou Got a BlackJack !")
                elif(language == "2"):
                        print("\nVocê Conseguiu um BlackJack !")
                myScore="BlackJack"
        elif(dealerScore == 21):
                if(language == "1"):
                        print("\nThe Dealer Got a BlackJack !")
                elif(language == "2"):
                        print("\nO Dealer Conseguiu Um  BlackJack !")
                dealerScore="BlackJack"
        
        # Player Turn Loop
        while(myScore != "BlackJack" and dealerScore != "BlackJack"):
                if(myScore <= 21 and dealerScore <= 21):
                        if(language == "1"):
                                case=input("\nInsert:\n ( c ) to Pick up a Card.\n ( p ) to Stop.\n ( s ) to Exit.\n")
                        elif(language == "2"):
                                case=input("\nInsira:\n ( c ) Para Pegar Uma Carta.\n ( p ) Para Parar.\n ( s ) Para Sair Do Jogo.\n")
                        if(case == "c"):
                                system('cls')
                                my.append(packCards[0]) , packCards.pop(0)
                                myScore = score(my)
                        elif(case == "p"):
                                system('cls')
                                if(language == "1"):
                                        print("You Stop With: %s" %myScore)
                                elif(language == "2"):
                                        print("Você Parou Com %s Pontos" %myScore)
                                break
                        elif(case == "s"):
                                exit()
                        system('cls')
                        if(language == "1"):
                                print("Your Cards:  ",end="")
                        elif(language == "2"):
                                print("Suas Cartas São:  ",end="")
                        for card in my:
                                print(card,end="  ")
                        if(language == "1"):
                                print("\nYour Score: %s" %myScore)
                                print("\nDealer's Cards:  %s   **" %dealer[0])
                        elif(language == "2"):
                                print(".\nVocê Possui %s Pontos" %myScore)
                                print("\nCartas Do Dealer:  %s  **" %dealer[0])
                else:
                        break
        
        # Dealer's Turn Announcement
        if(myScore != "BlackJack" and dealerScore != "BlackJack"):
                if(myScore <= 21):
                        if(language == "1"):
                                print("\nDealer's Turn !")
                                print("\nDealer Cards:  %s  %s" %(dealer[0],dealer[1]))
                        elif(language == "2"):
                                print("\nVez Do Dealer !")
                                print("\nCartas Do Dealer Viradas:  %s  %s" %(dealer[0],dealer[1]))

        # Dealer's Turn Loop
        while(myScore != "BlackJack" and dealerScore != "BlackJack"):
                if(myScore <= 21 and dealerScore <= 21):
                        if((((dealerScore > myScore or dealerScore == myScore) and dealerScore > 11) or dealerScore >= 18) and dealerScore <= 21):
                                if(language == "1"):
                                        print("\nThe Dealer Stop !")
                                elif(language == "2"):
                                        print("\nO Dealer Parou !")
                                break
                        else:
                                if(language == "1"):
                                        print("\nThe Dealer Pick up a Card !")
                                elif(language == "2"):
                                        print("\nO Dealer Pegou Uma Carta !")
                                dealer.append(packCards[0]) , packCards.pop(0)
                                dealerScore = score(dealer)
                                if(language == "1"):
                                        print("Dealer's Cards:  ",end="")
                                elif(language == "2"):
                                        print("Cartas Do Dealer:  ",end="")
                                for card in dealer:
                                        print(card,end="  ")
                                print()
                else:
                        break

        # End Game Conditional
        if(myScore != "BlackJack" and dealerScore != "BlackJack"):
                if(language == "1"):
                        input("\n\n( Continue... )")
                elif(language == "2"):
                        input("\n\n( Continuar... )")
                system('cls')
                if(language == "1"):
                        print("Dealer's Score: %s\nYour Score: %s" %(dealerScore,myScore))
                elif(language == "2"):
                        print("O Dealer tem %s Pontos\nVocê Tem %s Pontos" %(dealerScore,myScore))
                if((dealerScore > myScore and dealerScore <= 21) or (myScore > 21)):
                        if(language == "1"):
                                print("\nDealer Wins !")
                        elif(language == "2"):
                                print("\nO Dealer Venceu !")
                elif((myScore > dealerScore or dealerScore > 21) and myScore <= 21):
                        if(language == "1"):
                                print("\nYou Win !")
                        elif(language == "2"):
                                print("\nVocê Venceu !")
                elif(myScore == dealerScore):
                        if(language == "1"):
                                print("\nDraw !")
                        elif(language == "2"):
                                print("\nO jogo empatou !")

        # Input to Hold the Loop
        if(language == "1"):
                input("\n\n( Press any Key to Play Again... )")
        elif(language == "2"):
                input("\n\n( Pressione Qualquer Botão Para Jogar Novamente... )")