import random
def printer(x):
    i=0
    while (i<x):
        printf()
        i+=1


# welcome phrase 1
welcome = "Welcomed To CLF".center(120)
print(welcome)
printer(3)


# asking for the name
name = ''
while(name == ""):
    name = input(" « enter your name please » ")
    print()
printer(4)


# welcome phrase 2
name = name.upper()
welcome1 = " Hello "+name+' '
welcome1 = welcome1.center(120)
print(welcome1)
printer(4)

# NB of rounds
rounds = 0
while(rounds == 0) or (int(rounds) % 2 == 0):
    rounds = int(input("How many Rounds do you wanna play ? "))
    print()
print()


# Player class (frouda/zwez)
choice = ""
while (choice != 'F') and (choice != "Z"):
    choice = input("Choose 'F'/'Z' (frouda or zwez) ").upper()
    print()

pchoice = choice

# PC class (froud/zwez)
if pchoice == 'F':
    cchoice = 'Z'
else:
    cchoice = 'F'


# CLRSCR
def clrscr():
    response = input(
        "Wanna clear the screen before starting ? type 'yes to confirm '")
    if response == 'yes':


def clrscr2():
    response = input(" type 'continue' to proceed ")
    if response == 'continue':


clrscr()


fullscorec = fullscorep = 0

game = True
while game:
    scorep = scorec = 0
    for i in range(0, rounds):
        pickp = 6
        while pickp not in range(0, 6):
            pickp = int(input('Pick a number between 1 and 5: '))

        pickc = random.randint(0, 5)
        print()
        pickcreplica = str(pickc)
        print("the PC has chosen: "+pickcreplica)

        print()

        total = pickp+pickc

        if pchoice == 'F':
            if total % 2 == 0:
                scorec += 1
            else:
                scorep += 1
        else:
            if total % 2 == 0:
                scorep += 1
            else:
                scorec += 1

        print('total: ' + str(total))
        print('player score: ' + str(scorep))
        print('coputer score: ' + str(scorec))
        printer(4)

    if scorec > scorep:
        print(
            'oooh! did you just loose to a simple dumb Computer?! , Its so SAD, ALEXA play despacito ;(')
        print('Naah, just joking. Better luck next time ')
        fullscorec += 1
    else:
        print('WOW! did you just beat a Computer?! , you are so SMART !!!')
        fullscorep += 1
        printer(4)

    clrscr2()

    sfullscorec = str(fullscorec)
    sfullscorep = str(fullscorep)

    print('The score now is: you   ('+sfullscorep+'-'+sfullscorec+')   PC')
    rpt = input("Wanna Go AGAIN ? type 'yes' To Confirm: ")

    if not rpt == 'yes':
        game = False
    else:
