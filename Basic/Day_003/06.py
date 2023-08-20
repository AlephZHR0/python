print("Welcome to Brazil Lândia.")
print("""

  .''.
 (~~~~)
   ||
 __||__
/______\
  |  |' _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
  |  |'|o| - - - - - - - - - - - - - - - - - - - - - - - - -||
  |  |'| |                                                  ||
  |  |'| |                      . ' .                       ||
  |  |'| |                  . '       ' .                   ||
  |  |'| |              . '    .-'"'-.    ' .               ||
  |  |'| |          . '      ,"       ".      ' .           ||
  |  |'| |      . '        /:           :\        ' .       ||
  |  |'| |  . '            ;  .          ;            ' .   ||
  |  |'| |    ' .          \: . .       :/          . '     ||
  |  |'| |        ' .        `. . .    ,/       . '         ||
  |  |'| |            ' .      `-.,,.-'     . '             ||
  |  |'| |                ' .           . '                 ||
  |  |'| |                    ' .   . '                     ||
  |  |'| |                        '                         ||
  |  |'|o|-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_||
  |  |'
  |  |'
  |  |'
  |  |'
  '~~'
 
""")
print("Your mission is to find the carnaval.")
lr = input("You can choose betwen left and right, whats your choosen path?\n").lower()
if lr == "left":
    print("Nice choice, you arrived at the paredão on Morro do Sabão, the place you were was dangerous!")
    go_or_wait = input("You again have an option, Go trought the favela or Wait?\n").lower()
    if go_or_wait == "go":
        print("Ohh, you had been on the wrong place, you got luck, now they are having a fight against factions")
        which_one = input("You see three guys:\nRed t-shirt\nBlue t-shirt\nGreen t-shirt\n").lower
        if which_one == ("red"):
            print("You got the right guy, he knows tha way, and you two had a happy end on the carnaval and played some football on any favela")
        elif which_one == ("blue"):
            print("Hmmm, not a smart choice, but you hadn't knew, he drugged you and you died of cifilis")
        else:
            if input("Ok, I have a Good and a Bad news for you, wich one you want first?").lower() == "good":
                print("Ohh, you survived, but...\nA kid kicked the ball on your balls and you cant have kids anymore")
            else:
                print("A kid kicked the ball on your balls and you cant have kids anymore, but look at the good things in the life, you survived...")
    else:
        print("Oh noo, you decided to stood there, you got hit by a stray bullet")
else:
    print("Hmm, sorry, the traficante got you kidnapped!")
