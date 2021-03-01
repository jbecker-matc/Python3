#!/usr/bin/env python3

print("""Ye find yeself yon dark room with THREE doors. Do ye enter door #1, door #2, or door #3?""")


door = input("-> ")

# == Door Number 1 Logic ===================================
if door == "1":

     print("Ye see a flask sitting on a pedestal in the center of the room.")
     print("What do ye do?/n")

     print("1. Get ye flask.")
     print("2. Get ye flask.")

     # == Flask logic ======================================
     flask = input("-> ")

     if flask == "1":
          print("1) Ye can't get ye flask! Ye have to just sit there and imagine why on earth ye can't get ye flask.")
     elif flask == "2":
          print("2) Ye can't get ye flask! Ye have to just sit there and imagine why on earth ye can't get ye flask.")
     else:
          print(f"N)Ye just sit there and imagine why on earth ye can't get ye flask. I'm certainly not going to tell ye.")

# == Door Number 2 Logic ===================================
elif door == "2":

     print("Ye see a large beanstalk growing in the middle of the room, right through the ceiling.")
     print("What do ye do?/n")

     print("1. Climb ye beanstalk.")
     print("2. Take a nap in the shade.")

     # == Beanstalk logic ==================================
     beanstalk = input("-> ")

     if beanstalk == "1":
          print("1)Ye climb the beanstalk.")
          print("Keep climbing?\n")

          print("1. Yes")
          print("2. No")

     elif beanstalk =="2":
          print("2)Ye nap in the shade.")

     else:
          print(f"N)Ye imagine how tall the beanstalk could be.")

     # == Climbing logic ==============================
     while True:
          climbing = input("-> ")

          if climbing == "1":
               print("1)Ye climb the beanstalk.")
               print("Keep climbing?\n")

               print("1. Yes")
               print("2. No")

          elif climbing == "2":
               print("2)Ye can't find a way down.")
               print("Keep climbing?\n")

               print("1. Yes")
               print("2. No")
          else:
               print("Keep climbing?\n")

               print("1. Yes")
               print("2. No")

# == Door Number 3 logic ====================================
elif door == "3":

     print("Ye enter a room with a MaGiC pOrTaL!")
     print("what do ye do?\n")

     print("1. Enter yon MaGiC pOrTaL!")
     print("2. Do not enter yon MaGiC pOrTaL!")

     # == Portal logic ======================================
     Portal = input("-> ")

     if Portal == "1":
          print("1)Ye enter ye MaGiC pOrTaL! Good job!")
     elif Portal == "2":
          print("2)Ye do not enter yon MaGiC pOrTaL! Good job!")
     else:
          print("It's all glowy and... magicky")
