number = 5785
running = True

while running:
    guess = int(input("Ввгадай число"))
    if guess == number:
        print("Вгадав")
        running = False
    elif guess < number:
        print("мало")
    else:
        print("багато")
