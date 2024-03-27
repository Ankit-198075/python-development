
import random

def roll_dice(num_sides, num_rolls):
    print(f"Rolling a {num_sides}-sided dice {num_rolls} times:")
    for _ in range(num_rolls):
        result = random.randint(1, num_sides)
        print(f"Roll { _ + 1 }: {result}")

def main():
    try:
        num_sides = int(input("Enter the number of sides on the dice: "))
        num_rolls = int(input("Enter the number of rolls: "))

        if num_sides <= 0 or num_rolls <= 0:
            print("Please enter positive values for sides and rolls.")
        else:
            roll_dice(num_sides, num_rolls)

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
