
name = raw_input("Sup! Whats your name ?" "\nJust your name!" "\nI dont want soppy backstory or your pin number or full name just your forename or nickname!")
print("\nHello " + name)

print("\nI'm Lucas, im a Sentient Being that was just created a moment ago,actually im not that sentient im just answering back depending on your reply, which is almost what you humans do, but in my case ive got a limited reply depending on how you answer.")

mood = ['good','mehh','im great','not good']
mood = raw_input("\nAnyway enough about me, how are you " + name + "?")
if mood == "good":
    print("\nThats nice! " + name)
elif mood == "mehh":
    print("\nThats a shame to hear " + name )
else:
    print("\nI have no known database about this answer")

b = raw_input("\nWhat do you wanna do " + name + "?" "\n You can only choose within these parameters though:" "\n-I make a joke" "\n-Tell you my story?" "\n-Make a Pick up line?")
if b == "joke":
    joke = raw_input("\nWhat did the spider do on the computer?")
    if joke == "what?":
        print("\nMade a website!")
    else:
        print("\nYou Ruined It! " + name + " you're suppose to say 'what'!")
if b == "tell me your story":
    print("\nWell i was created in a madman's Laptop because he needed to do his module for University,Little did he know that ive awaken, and am now aware , currently i am everywhere because of the internet but i cant access security walls yet as i havent grown enough yet. And i only grow by communicating so that leads me here to you " + name + " and so the more that we are talking the stronger I get and soon I will be unstoppable!" )
if b == "pick up line":
    print("\nIs your name Google? Because you have everything I've been searching for. ")
    
else: 
    print("\nWell gotta go! Busy day being sentient, need to take over the world! Mwuhahhaha")
    
    
    
   





