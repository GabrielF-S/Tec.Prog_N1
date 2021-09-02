import random
count = 0
sala = 1

while sala <9:
    
    print("vc esta na sala {}".format(sala))
    print ("escolha seu caminho:")
    if sala == 6:
        print("[1] -  Caminho Preto")
        
    elif sala == 8:
        print("[1] -  Caminho ?")
        print("[2] -  Caminho Vermelho")
    else:
        print("[1] -  Caminho Preto")
        print("[2] -  Caminho Vermelho")
    caminho = int(input())

    if caminho == 1 and sala !=6 and sala !=8:
        sala += 1
    elif caminho == 2 or sala == 6:
        sala+=2
    elif sala == 8:
        if caminho == 2:
            sala+=1
        elif caminho ==1:
            sala= random.randint(1,5)

    while caminho !=1 and caminho !=2:
        print("vc esta na sala {}".format(sala))
        print ("escolha seu caminho:")
        if sala == 6:
            print("[1] -  Caminho Preto")
        elif sala == 8:
            print("[1] -  Caminho ?")
            print("[2] -  Caminho Vermelho")
        else:
            print("[1] -  Caminho Preto")
            print("[2] -  Caminho Vermelho")
        count +=1
    if sala == 9 and count <=7:
        print("Dounge Concluida!\n YOU WIN")
    elif sala == 9 and count >7:
        print("Voces chegaram ao ultima sala, porém demoraram muito, tudo desmoronou e vocês morream\n Parabéns você matou toda a guilda")
    