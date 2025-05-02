import random  # Import the random module, which allows us to generate random numbers.

def number_guessing_ai():
    # Defining a Function to run the Number Guessing AI game
    print("The Number Guessing AI welcomes you!")  # Welcome message for the player
    print("Select a range to guess:")  # Prompt user to choose a range
    print("1. Between 1 and 50")  # Option 1: Range from 1 to 50
    print("2. Between 1 and 100")  # Option 2: Range from 1 to 100

    # Get the user's choice for the range by reading input
    choice = input("Enter 1 or 2: ")  # Takes input from the user as a string (1 or 2)
    
    # Determine the upper limit for the random number based on user's choice
    # If user entered "1", max_number will be 50; otherwise, it will be 100.
    max_number = 50 if choice == "1" else 100
    
    # Generate a random target number within the selected range (1 to max_number)
    # random.randint(a, b) returns a random integer between a and b (inclusive).
    random_number = random.randint(1, max_number)
    
    # Initialize a counter for the number of attempts the player makes.
    attempts = 0  # Initially, the player has made 0 attempts.

    # Inform the player about the chosen range
    print(f"I've picked a number between 1 and {max_number}. Attempt to predict it!")

    # Start a loop that will continue until the player guesses the target number
    while True:
        # Get the user's guess by reading input and converting it to an integer
        guess = int(input("Put in your guess: "))
        
        # Increment the attempts counter by 1 for each guess made by the player
        attempts += 1

        # Check if the guess is equal to the target number
        if guess == random_number:
            # If the guess is correct, print a success message and the number of attempts
            print(f"Well done! You made {attempts} guesses about the number.")
            break  # Exit the loop since the correct number was guessed
        
        # If the guess is incorrect, provide feedback based on how close it is to the target
        elif abs(random_number - guess) <= 3:
            # If the absolute difference between guess and target number is 3 or less, they're very close
            print("You're very close!")
        
        elif abs(random_number - guess) <= 10:
            # If the difference is 10 or less, the guess is somewhat close
            print("You're getting closer!")
        
        elif abs(random_number - guess) <= 20:
            # If the difference is 20 or less, the guess is a bit far from the right answer
            print("You're a bit far")
        
        else:
            # If the difference is greater than 20, the guess is far off
            print("You're far away")
        
        # Print a message encouraging the player to try again after each incorrect guess
        print("Give it another try")

# Run the program by calling the function
number_guessing_ai()
