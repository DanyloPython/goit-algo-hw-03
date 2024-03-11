import random

def generate_winning_numbers(min, max, quantity):

    return random.sample(range(min, max+1), quantity)

def get_user_numbers():
   
    user_input = input("Введіть три числа через кому (наприклад, 5, 12, 24): ")
    user_numbers = [int(number.strip()) for number in user_input.split(',')]
    return user_numbers

winning_numbers = generate_winning_numbers(1, 30, 3)

user_numbers = get_user_numbers()
print("Ваші числа:", user_numbers)

if sorted(user_numbers) == sorted(winning_numbers):
    print("Вітаю, ви вгадали!")
    print(f"Виграшні числа: {winning_numbers}")
else:
    print("На жаль, ви не вгадали. Спробуйте ще раз!")
    print(f"Виграшні числа: {winning_numbers}")

