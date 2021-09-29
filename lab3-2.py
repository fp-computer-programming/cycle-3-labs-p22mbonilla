# Author MB 09/29/2021

x = int(input("how many point did they make"))

if x >= 15:
    print("you GOT A GOLD medal")
elif x >= 12:
    print("YOU WON A silver MEDAL")
elif x < 9:
    print("bronze medal for you")
else:
    print("no medal for you")
