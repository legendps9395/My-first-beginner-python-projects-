print("Hello welcome to priyanshu coffee shop ")
name = input("what is your name?\n" ).title()
if name == "Bob":
    evil_status = input("Are you evil?\n").lower
    good_deeds = int(input("How many good deeds have you done today?\n"))
    if evil_status == "yes" and good_deeds <4 :
        print("You are not welcome here, get out from here")
        exit()
    if evil_status == "no":
     print("Oh! so you are one of those good Bobs. You are welcome here")
else : print("Hello " + name + " thank you so much for coming in today!!")
menu = "Black Coffee :- $3,\n Espresso :- 4$,\n Latte :- $6,\n Cappucino :- $6.5,\n Frappuchino :- $7.5,\n Classical Coffee :- $2"

print(name + ", What would you like from our menu today? "
"Here is what we are serving today.\n" + menu  )
while True:
    order = input().lower()
    if order == "black coffee":
        price = 3
        break
    elif order == "espresso":
        price = 4
        break
    elif order == "latte":
        price = 6
        break
    elif order == "cappuchino":
        price = 6.5
        break
    elif order == "frappuccino":
        price = 7.5
        break
    elif order == "classical coffee":
        price = 2
        break
    else:
        print("Sorry, we don't have that.\nPlease choose anything above from menu")

quantity = input("How many " + order.title() + " would you like?\n")
total = price * int(quantity)
print ("Your total is: $" + str(total))
print("Sounds good, we will have your " + quantity +" "+ order + " ready in a moment") 

