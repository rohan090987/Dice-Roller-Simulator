import random
import time
import os

def roll_dice():
    print("Rolling the dice", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()
    time.sleep(0.5)
    result = random.randint(1, 6)
    print(f"\n🎲 You rolled a {result}!\n")

def main():
    while True:
        input("Press Enter to roll the dice (or type 'q' and hit Enter to quit): ")
        roll_dice()
        again = input("Roll again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
