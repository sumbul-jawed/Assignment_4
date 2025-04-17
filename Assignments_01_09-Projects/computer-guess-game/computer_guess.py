import random
print("\n ✨Welcome to the Number Guessing Game.✨ \n") 

low = 1
high = 10

print("🤔 Think of a number between 1 and 10, and 💻 will try to guess it!")
if low <= high:
    guess = random.randint(low, high)
    print("🤖 computer guess is: ", guess)

    while True:
        feedback = input("Is the guess is too high (H), too low (L), or correct (C)? ").strip().upper()
       
        if feedback == 'C':
           print("yay! The computer guessed your number correctly. ")
           break

        elif feedback == 'H':
         high = guess - 1
         guess = random.randint(low, high)
         print("computer's guess is: ", guess)

        elif feedback == 'L':
         low = guess + 1
         guess = random.randint(low, high)
         print("computer's guess is: ", guess)
        else:
         print("⚠️ Invalid input. Please enter only 'H', 'L', or 'C'. 🚫")

if low > high:
    print("😅 Hmm... It seems there was a misunderstanding. Let's try again! 🔄")