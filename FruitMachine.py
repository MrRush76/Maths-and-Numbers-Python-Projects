import os
import time
import random

def spin(credits):
  credits -= 20
  if credits >= 20:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"You have {credits} credits\n")
    time.sleep(0.6)
    print("Spinning...")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("* * *")
    time.sleep(0.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(". . .")
    time.sleep(0.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    icons = ['🍒', '🍋', '🍉', '🍇', '💀' , '🔔']
    result = [random.choice(icons) for _ in range(3)]
    print(" ".join(result))
    cherry_count = result.count('🍒')
    if cherry_count > 0:
      print(f"You win {20 * cherry_count} credits")
      credits += 20 * cherry_count
    elif result == ['🍋', '🍋', '🍋']:
      print("You win 40 credits")
      credits += 40
    elif result == ['🍉', '🍉', '🍉']:
      print("You win 30 credits")
      credits += 30
    elif result == ['🍇', '🍇', '🍇']:
      print("You win 20 credits")
      credits += 20
    elif result == ['💀', '💀', '💀']:
      print("You lose 100 credits")
      credits -= 100
    elif result == ['🔔', '🔔', '🔔']:
      print("You win 100 credits")
      credits += 100
    else:
      print("You didn't win this time! Press Enter to play again or 'n' to quit")
      playagain = input()
      if playagain.lower() == "n":
        print("Thanks for playing!")
        return
      else:
        spin(credits)
    print(f"You now have {credits} credits")
    if credits < 20:
      print("You don't have enough credits to continue playing!")
      time.sleep(1)
      fruit_machine()
    else:
      print("Press Enter to spin again or 'n' to quit")
      playagain = input()
      if playagain.lower() == "n":
        print("Thanks for playing!")
        return
      spin(credits)
  else:
    print("You don't have enough credits to continue playing!")
    time.sleep(1)
    fruit_machine()

def fruit_machine():
  os.system('cls' if os.name == 'nt' else 'clear')
  print("🎰 Welcome To The Fruit Machine 🎰\n")
  print("💰You Have 100 Credits💰\n")
  print("💸Each Spin Costs 20 Credits💸\n")
  time.sleep(2)
  spininput = input("Press Enter to Spin\n")
  if spininput == "":
    spin(100)
  else:
    print("Invalid input")
    time.sleep(1)
    fruit_machine()

os.system('cls' if os.name == 'nt' else 'clear')
fruit_machine()
