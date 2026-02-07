print("Welcome to Treasure Island. Your mission is to find the treasure.")
left_or_right = input("Left or Right? L/R : ").lower()

if left_or_right != "l":
    print("You fell into a hole. Game Over.")
else:
    swim_or_wait = input("Swin or Wait? S/W : ").lower()
    if swim_or_wait != "w":
        print("Attacked by trout. Game Over.")
    else: 
        door = input("Which door? Red, Blue or Yellow? R/B/Y : ").lower()
        if door == "y":
            print("You Win!")
        elif door == "r":
            print("Burned by fire. Game Over.")
        elif door == "b":
            print("Eaten by beasts. Game Over.")
        else:
            print("Game Over.")