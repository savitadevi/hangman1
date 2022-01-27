from words import choose_word
from image import IMAGES

def hangman():
    
    secret_word=choose_word()
    guessmade=""

    print(secret_word)

    turns=(len(secret_word))
    print()
    # secret_word=choose_word
    print(len(secret_word))
    while len(secret_word)>=0:
        main_word=""

        for letter in secret_word:

            if letter in guessmade:
                main_word=main_word+letter
            else:
                main_word=main_word+  " _ "
        if main_word==secret_word:
            print("the word was ",main_word)
            print("you won")
            break
        print("guess the word",main_word)
        guess=input("enter your seackret word")
        if guess in secret_word:
            guessmade=guessmade+guess
        else:
            print("enter validcharacter")
            if guess not in secret_word:
                turns=turns-1
            if turns==len(secret_word)-1:
                print(turns,"turns left")
                print(IMAGES[0])
            if turns==len(secret_word)-2:
                print(turns,"turns left")
                print(IMAGES[1])
            if turns==len(secret_word)-3:
                print("turns left")
                print(IMAGES[2])
            if turns==len(secret_word)-4:
                print(turns,"turns left")
                print(IMAGES[3])
            if turns==len(secret_word)-5:
                print(turns,"turns left")
                print(IMAGES[4])
            if turns==len(secret_word)-6:
                print(turns," turns left")
                print(IMAGES[5])
            if turns==len(secret_word)-7:
                print(turns," turns left")
                print(IMAGES[6])
            if turns==len(secret_word)-8:
                print(turns,"turns left")
                print(IMAGES[7])
                print("you lose the game")
                break
            
                

            # if turns==len(secret_word)-9:
            #     print(turns,"turns left")
            #     print(IMAGES[8])
                



            

name=input("ENTER THE NAME-->")
print("welcome",name,"!!")
print("-------------------------") 
print("try to guess the word in attempts")
hangman()
