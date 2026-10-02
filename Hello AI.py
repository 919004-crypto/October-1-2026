print("Hello, I am an AI bot, what is your name? ")
name =input()
print(f"{name}, how are you feeling today(good/bad)")
mood = input()

if mood == "good":
    print("I'm glad to hear that.")
elif mood == "bad":
    print("I'm sorry to hear that.")
else:
    print("I know it is hard to put your feelings in words.")

print(f"Bye {name}")