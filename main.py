
import dice

# GAME DICE
D4 = dice.Dice(4)
D6 = dice.Dice(6)
D8 = dice.Dice(8)
D12 = dice.Dice(12)
D20 = dice.Dice(20)


def main():
   print("Hello!  Welcome to our Character Creator!")


   rollAndPrint(D4)
   rollAndPrint(D6)
   rollAndPrint(D8)
   rollAndPrint(D12)
   rollAndPrint(D20)


def rollAndPrint(theDice):
    value = theDice.roll()
    print("I rolled: " + str(value));


if __name__== "__main__":
    main()