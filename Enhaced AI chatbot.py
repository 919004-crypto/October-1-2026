chatting = True

while chatting:
    print("Hello! I am a simple chatbot.")
    
    name = input("What is your name? ")
    print("Nice to meet you, " + name + "!")
    
    mood = input("How are you feeling today? (good/bad/tired): ")
    
    if mood == "good":
        print("That is awesome to hear!")
    elif mood == "bad":
        print("I am sorry to hear that. I hope it gets better!")
    elif mood == "tired":
        print("Make sure to get some rest!")
    else:
        print("Thanks for sharing!")
        
    topic = input("Do you like coding? (yes/no): ")
    if topic == "yes":
        print("Me too! Python is my favorite.")
    else:
        print("That is okay, everyone has different hobbies!")
        
    repeat = input("Do you want to chat again? (yes/no): ")
    if repeat == "no":
        chatting = False
        print("Goodbye, " + name + "!")
    print()
