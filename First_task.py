from datetime import datetime

def get_days_from_today(date):
    try:
        date = datetime.strptime(date, '%Y-%m-%d')
        current_date = datetime.today()
        delta = current_date - date
        return abs(delta.days)
    except ValueError:
        return "На жаль, Ви ввели невірний формат дати. Будь ласка, введіть дату ще раз у форматі РРРР-ММ-ДД."

date = input("Введіть дату у форматі РРРР-ММ-ДД: ")
print(f"Різниця становить:{get_days_from_today(date)}")