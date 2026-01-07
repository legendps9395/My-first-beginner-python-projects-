import time
print("Hello welcome to priyanshu coffee shop ")
name = input("what is your name?\n" ).title()

if name == "Bob":
     while True:
               evil_status = input("Are you evil?\n").lower()
               if evil_status == "yes":
                    while True:
                         try:
                              good_deeds = int(input("How many good deeds have you done today?\n"))
                              break
                         except ValueError:
                              print("enter a valid number")
                    if evil_status == "yes" and good_deeds <4 :
                         print("You are not welcome here, get out from here")
                         time.sleep(3)
                         exit()
                    else:
                         print("Oh! so you are one of those good Bobs. You are welcome here")
                         break
               elif evil_status == "no" :
                    print("Oh! so you are one of those good Bobs. You are welcome here")
                    break
               else:
                    print("Give a proper answer.")
else : print("Hello " + name + " thank you so much for coming in today!!")
    
menu = "Black Coffee :- $3,\n Espresso :- 4$,\n Latte :- $6,\n Cappuccino :- $6.5,\n Frappuccino :- $7.5,\n Classical Coffee :- $2"
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
    elif order == "cappuccino":
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
while True:
     try:
          quantity = int(input("How many " + order.title() + " would you like?\n"))
          break
     except ValueError:
          print("Enter only a valid number.")
total = price *(quantity)
print (f"Your total is: $ {total:.2f}")
print(f"Sounds good, we will have your {quantity} {order} ready in a moment") 

