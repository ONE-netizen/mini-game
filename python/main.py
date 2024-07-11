import random
min_n = 0
max_n = 100
bot_n = random.randint(min_n, max_n)
count_us = 7

print(f"Начало игрыю Тебе нужно будет угадать число от {min_n} до {max_n}")

while True:
    if count_us == 0:
       print(f"К сожалению попытки кончились :( Загадонное число было {bot_n}")
       break

    user_ans = int(input(f"У вас {count_us} попыток! Попробуйте угадать число :   "))

    if user_ans > bot_n:
        print("Ваше число больше чем загаданное...")
    elif user_ans < bot_n:
        print("Ваше число меньше чем загаданное...")
    elif user_ans == bot_n:
        print("Вы угадали!")
        break

    count_us -= 1