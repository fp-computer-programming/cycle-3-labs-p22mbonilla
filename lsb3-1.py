# Author MB 09/29/2021

x = int(input("how many point did they make"))

if x >= 15:
    print("you GOT A GOLD medal")
else:
    if x >= 12:
        print("YOU WON A silver MEDAL")
    else:
        if x < 9:
            print("No medal for you")
        else:
            print("you won a bronze")
