import random

print("""
Each powerball lottery ticket costs $2. The jackpot for this game is $1.586 billion! It doesnt matter what the jackpot is, though, 
because the odds are 1 in 292,201,338, so you won't win.

This simulation gives you the thrill of playing without wasting money.
""")

# Let the player enter the first five numbers, 1 to 69
while True:
    print('Enter 5 different numbers from 1 to 69 with spaces between')
    print("Example: 5 17 25 3 9")
    response = input("> ")

    # Make sure the player entered 5 numbers
    numbers = response.split()
    if len(numbers) != 5:
        print("Please try again.")
        continue

    try:
        for i in range(5):
            numbers[i] = int(numbers[i])
    except ValueError:
        print("Do it right, moron.")
        continue

    # Make sure numbers are between 1 and 69
    for i in range(5):
        if not(1 <= numbers[i] <= 69):
            print("The numbers need to be between 1 and 69.")
            continue

    # Make sure all numbers are unique. We will create a set.
    if len(set(numbers)) != 5:
        print("You need to enter 5 unique numbers")
        continue

    break

# Let the player select the powerball, 1 to 26
while True:
    print("Enter the powerball number, 1 to 26.")
    response = input(">")

    # Convert strings to integers
    try:
        powerball = int(response)
    except ValueError:
        print("You screwed something up. Good work.")
        continue

    # Make sure its between 1 and 26
    if not (1 <= powerball <= 26):
        print("Powerball must be between 1 and 26.")
        continue

    break

# Enter number of times you want to play:
while True:
    print("How many times do you want to play? (Max: 1000000)")
    response = input('>')

    # Convert strings to integers
    try:
        numplays = int(response)
    except ValueError:
        print("Pick a number, idiot.")
        continue

    # See if number is between 1 and 1000000
    if not (1 <= numplays <= 1000000):
        print("Number chosen was either too high or too low")
        continue

    break

# Run the simulation
price = "$" + str(2 * numplays)
print('It costs', price, 'to play', numplays, 'but dont worry, Im sure you will make it all back')
input('Press enter to start')

possibleNumbers = list(range(1, 70))
for i in range(numplays):
    # Come up with winning numbers
    random.shuffle(possibleNumbers)
    winningNumbers = possibleNumbers[0:5]
    winningPowerball = random.randint(1, 26)

    # Display winning numbers
    print("The winning numbers are: ", end='')
    allWinningNums = ''
    for i in range(5):
        allWinningNums += str(winningNumbers[i]) + ' '
    allWinningNums += 'and ' + str(winningPowerball)
    print(allWinningNums.ljust(21), end='')
    if set(numbers) == set(winningNumbers) and powerball == winningPowerball:
        print()
        print('You have won the powerball lottery! Congrats!')
        print('You would be a billionaire if this was real')
        break
    else:
        print(" You lost.")

print('You have wasted', price)
print('Thanks for playing!')
