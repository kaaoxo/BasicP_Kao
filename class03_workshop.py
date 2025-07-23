mon = 100
weap1 = 20
weap2 = 10
weap3 = 15
gamestart = True


while gamestart:
    print("welcome to kiritu program")
    print("choose the option")
    print("1.fight")
    print("2.Escape")
    x = int(input("Your choice is : "))
    if x == 2:
        print("Exit")
        gamestart = False
    elif x == 1:
     round = int(input("How many round :" ))
     r = round
     for i in range (round):
        print("choose your weapon :")
        print("weapon1 damage : 20")
        print("weapon2 damage : 10")
        print("weapon3 damage : 15")
        weap = input("your weapon is ")
        if weap == "weap1":
           mon -= 20
        elif weap == "weap2":
           mon -= 10
        elif weap == "weap3":
           mon -= 15
        r -= 1
        print(mon)
        print("round left : ",r)
        if mon < 0:
            mon += 20
            print("Monster still alive")
        elif mon == 0:
           print("Monster Died and You win")
        if i == round and mon > 0:
           print("You Died")
        gamestart = False
    gamestart = False
     
     
     
     
    
    

