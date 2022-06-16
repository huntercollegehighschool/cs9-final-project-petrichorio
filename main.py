"""
Name(s):Deetya, Georgie
Name of Project:Final Project
"""

#Write the main part of your program here. Use of the other pages is optional.
import random


def part1():
  print("You are in a dark room. You see a door, a rug, and a locked box. You can search under the rug, try to open the door, or try to open the box.")
  choice = input("Enter R to search under the rug, D to open the door, B to check out the box, or type anything to go back to the start.")
## 1st part
  if choice == "R":
    def rug():
      lis = ["1100101010010↓2","1952↓16", "4aWS↓64", "-.... ....- ---.. ..---"]
      print("You find a piece of paper with a message:", random.choice(lis), "You can try to use this code elsewhere")
    print( rug(), part1())
# 2nd part
  elif choice == "S":
    return part1()
# 3rd part
  elif choice == "B":
    def box():
      c = int(input("You find a 4 digit lock on the box. Input a code to try on the box: "))
      k = c
      if c == 6482:
        print("You found a key!")
        choice2 = input("You can now try it on the door, or go back to start. To try the door, press n. To go back to start, press m.")
        if choice2 == "n":
            print("congrats! you found a way out")
        else:
            return part1()
      else:
        print("That's not the right code. Make sure it's 4 digits and typed correctly.")
        return part1()    
    return box()
  #part 4
  elif choice == "D":
    print ("The door is locked.")
    return part1()
  else:
    print ("That's not an option. Make sure you capitalize your choice.", part1())
print (part1())
#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4
