import os, random, time

print("HOT DOG TYCOON") # y'a pas d'emoji dans windows
print("==============")

input("Press enter to start: ")

orders = 0 # comme le nieveau mais compteur de commandes
money = 0
state = "Day"
day = 1

toppings = {
    "sausage": ["Normal", "Vegan", "Kosher"], # y'a bcp de feujs aux USA Kosher = Casher
    "sauce": ["Ketchup", "Mustard"],
    "bread": ["Sesame", "Normal"],
    "nbrSausages": ["1", "2"] # Wow pas triple on le debloque plus tard
}

command = {
    "sauce": random.choice(toppings["sauce"]).lower(),
    "bread": random.choice(toppings["bread"]).lower(),
    "sausage": random.choice(toppings["sausage"]).lower(),
    "nbrSausages": random.choice(toppings["nbrSausages"]).lower()
}

stuff = {
    "sesame bread" : 10,
    "normal bread" : 10,
    "ketchup" : 10,
    "mustard" : 10,
    "normal sausage" : 10,
    "vegan sausage" : 10,
    "kosher sausage" : 10,
    "vegan sausage" : 10
}

prices = {
    "bread" : random.random(0.30, 0.99),
    "sauce" : random.random(0.01, 0.50)
}

def whatsInShop():
    print("1 Bread = $", prices[0])
def shuffleCommand():
    global command
    command = {
    "sauce": random.choice(toppings["sauce"]).lower(),
    "bread": random.choice(toppings["bread"]).lower(),
    "sausage": random.choice(toppings["sausage"]).lower(),
    "nbrSausages": random.choice(toppings["nbrSausages"]).lower()
    }

def cook():
    print("\nCOOK\n====")
    cookResult = [str(input("Write the kind of bread in this hot-dog : ")).lower(),
                  str(input("Write the number of sausages in this hot-dog : ")),
                  str(input("Write the kind of sausage in this hot-dog : ")).lower(),
                  str(input("Write the sauce of this hotdog : ").lower())
                 ]
    for i in range(0, 4):
        suff[cookResult[i]] -= 1
    return cookResult

def Order():
    price = 0
    global money
    global orders
    order = [command["bread"], command["nbrSausages"], command["sausage"], command["sauce"]]
    startTime = int(time.time()) # on en as besoin
    print("\nNEW ORDER!\n=========\nBread: ", order[0], "\nSausage(s): ", order[1], order[2], "\nSauce: ", order[3])
    hotdog = cook()
    endTime = int(time.time())
    if hotdog[0] == order[0]:
        price += 0.70
    if hotdog[2] == order[2]:
        price += int(order[1]) * 1
    if hotdog[3] == order[3]:
        price += 0.30
    price += 10 / (endTime - startTime)
    price = round(price, 2)
    print("You got $",price," with this hotdog!")
    money += price
    orders += 1
    shuffleCommand()

def main():
    os.system("clear")
    global day
    global state
    global money
    oldMoney = money
    print("HOT DOG TYCOON")
    print("==============")
    print("It's the ", state)
    print(f"It's your {day}TH as a hot dogger")
    print(f"Money : {money}")
    print(f"Orders so far : {orders}")
    if state == "Day":
        for i in range(0, random.randint(1, 10)):
            Order() #BOOM grosse func sans args !!
        print("Finally The End of the day !")
        print("You've made $", (money - oldMoney), " today !")
        print("It's now the night, go buy toppings to have enough food tomorrow")
        input("Press enter to continue > ")
        state = "Night"
    else:
       pass     
while True:
    main()