x = int(input("Enter any number: "))
#The basics
def number_play(x):
    #x = int(input("Enter any number: "))
    if x < 0:
        x = 0
        print('Negative changed to zero')
    elif x == 0:
        print('Zero')
    elif x == 1:
        print('Single')
    else:
        print('More')

number_play(x)
