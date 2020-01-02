
import dice
import character

# GAME DICE
D4 = dice.Dice(4)
D6 = dice.Dice(6)
D8 = dice.Dice(8)
D12 = dice.Dice(12)
D20 = dice.Dice(20)

GUY = character.Character()


def main():
    print("Hello!  Welcome to our Character Creator!")

    v = D20.rollAndAdd(20)
    print(str(v))

    v = D20.rollAndAverage(20)
    print(str(v))

    GUY.name = input("What is your character's name?: ")
    print("Great!  You created: " + GUY.name)


if __name__ == "__main__":
    main()
