from random import choice
from os import system
while(True):
        baralho,nrpt,meu,dealer=[],[],[],[]
        dpts=mpts=x=AA=BB=a=0
        naipe,num=("\u2665","\u2660","\u2666","\u2663"),("A","2","3","4","5","6","7","8","9","10","J","Q","K")
        while(x<52):
                carta=choice(num)+choice(naipe)
                if(not carta in nrpt):
                        baralho.append(carta),nrpt.append(carta)
                        x+=1
        def conta (A,B):
                soma=0
                if(A[B][0]=="J" or A[B][0]=="Q" or A[B][0]=="K"):
                        soma+=10
                elif(A[B][0]=="A"):
                        soma+=11
                elif(A[B][0]=="1"):
                        soma+=10
                elif(A[B][0]!="A" and A[B][0]!="J" and A[B][0]!="Q" and A[B][0]!="K"):
                        soma+=int(A[B][0])
                return soma
        for x in range (2):
                meu.append(baralho[0]),baralho.pop(0),dealer.append(baralho[0]),baralho.pop(0)
                mpts+=conta(meu,x)
                if(meu[x][0]=="A"):
                        AA+=1
                dpts+=conta(dealer,x)
                if(dealer[x][0]=="A"):
                        BB+=1
        print("Suas Cartas Iniciais São:  %s e %s."%(meu[0],meu[1]))
        print("Você Possui: %s Pontos."%mpts)
        if(mpts==21):
                print("\nBlackJack !")
                mpts="BlackJack"
        elif(dpts==21):
                print("\nO Dealer Conseguiu Um  BlackJack !")
                dpts="BlackJack"
        elif(True):
                print("Cartas Do Dealer:  %s e **."%dealer[0])
        while(mpts!="BlackJack" and dpts!="BlackJack"):
                if(mpts<=21 and dpts<=21):
                        escolha=input("\nInsira:\n ( c ) Para Pegar Uma Carta.\n ( p ) Para Parar.\n ( s ) Para Sair Do Jogo.\n")
                        if(escolha=="c"):
                                meu.append(baralho[0]),baralho.pop(0)
                                if(meu[len(meu)-1][0]=="A"):
                                        AA+=1
                                print("Suas Cartas São:  ",end="")
                                for x in range(len(meu)):
                                        print(meu[x],end="  ")
                                mpts+=conta(meu,len(meu)-1)
                                if(AA>=1 and mpts>21):
                                        mpts-=10
                                        AA-=1
                                system('cls')
                                print(".\nVocê Possui: %s Pontos."%mpts)
                        elif(escolha=="p"):
                                system('cls')
                                print("Você Parou Com %s Pontos."%mpts)
                                break
                        elif(escolha=="s"):
                                exit()
                        else:
                                system('cls')
                                print("Suas Cartas São:  ",end="")
                                for x in range(len(meu)):
                                        print(meu[x],end="  ")
                                print(".\nVocê Possui: %s Pontos."%mpts)
                                print("Cartas Do Dealer:  %s e **."%dealer[0])
                        if(mpts!="BlackJack" and mpts>21):
                                print("\n\nO Dealer tem: %s Pontos.\n Você Tem: %s Pontos."%(dpts,mpts))
                                print("\nO Dealer Venceu !")
                                x=111
                                break
                else:
                        break
        if(mpts!="BlackJack" and dpts!="BlackJack"):
                if(mpts<=21):
                        print("\nVez Do Dealer...")
                        print("Cartas Do Dealer Viradas: %s e %s"%(dealer[0],dealer[1]))
        while(mpts!="BlackJack" and dpts!="BlackJack"):
                if(mpts<=21 and dpts<=21):
                        if((((dpts > mpts or dpts == mpts) and dpts > 11) or dpts >= 18) and dpts <= 21):
                                print("\nO Dealer Parou !")
                                break
                        else:
                                print("\nO Dealer Pegou Uma Carta !")
                                dealer.append(baralho[0]),baralho.pop(0)
                                if(dealer[len(dealer)-1][0]=="A"):
                                        BB+=1
                                dpts+=conta(dealer,len(dealer)-1)
                                if(BB>=1 and dpts>21):
                                        dpts-=10
                                        BB-=1
                                print("Cartas Do Dealer:  ",end="")
                                for x in range (len(dealer)):
                                        print(dealer[x],end="  ")
                else:
                        break
        if(x!=111 and (mpts!="BlackJack" and dpts!="BlackJack")):
                print("\n\nO Dealer tem: %s Pontos.\nVocê Tem: %s Pontos."%(dpts,mpts))
        if(mpts!="BlackJack" and dpts!="BlackJack"):
                if(dpts>mpts and dpts<=21):
                        print("\nO Dealer Venceu !")
                elif((mpts>dpts or dpts>21) and mpts<=21):
                        print("\nVocê Venceu !")
                elif(mpts==dpts):
                        print("\nO jogo empatou !")
        input("\n\n( Pressione Qualquer Botão Para Jogar Novamente... )")
        system('cls')
