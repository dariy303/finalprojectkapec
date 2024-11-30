import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import sqlite3

class usd:
    def __init__(self):
            self.response = requests.get('https://minfin.com.ua/ua/currency/')
            if self.response.status_code == 200:
                soup = BeautifulSoup(self.response.text, features='html.parser')
                soup_list = soup.find_all("div", {"class":"sc-1x32wa2-9 bKmKjX"})

                self.total = str(soup_list[0]).split('<')[1].split(">")[1]
                self.total = self.total.replace(',', '.')
class euro:
    def __init__(self):
            self.response = requests.get('https://minfin.com.ua/ua/currency/')
            if self.response.status_code == 200:
                soup = BeautifulSoup(self.response.text, features='html.parser')
                soup_list = soup.find_all("div", {"class":"sc-1x32wa2-9 bKmKjX"})

                self.total = str(soup_list[3]).split('<')[1].split(">")[1]
                self.total = self.total.replace(',','.')
class pl():
    def __init__(self):
            self.response = requests.get('https://minfin.com.ua/ua/currency/')
            if self.response.status_code == 200:
                soup = BeautifulSoup(self.response.text, features='html.parser')
                soup_list = soup.find_all("div", {"class":"sc-1x32wa2-9 bKmKjX"})

                self.total = str(soup_list[6]).split('<')[1].split(">")[1]
                self.total = self.total.replace(',','.')

# Функція для обміну валют
def convert_currency():
    try:
        amount = float(amount_entry.get())  # Отримуємо значення суми
        to_currency = to_currency_var.get()  # Валюта, на яку обмінюємо

        # Статичні курси валют
        rates = {
            'USD': usd().total,   # Відносно долара США
            'EUR': euro().total,  # Євро
            'HAMSTR': 0.000000000000000001,
            'pl': pl().total,

        }

        # Переведення суми відповідно до вибраних валют
        if to_currency == 'EUR':
            result = amount / float(rates['EUR'])
        elif to_currency == 'HAMSTR':
            result = amount / float(rates['HAMSTR'])
        elif to_currency == 'USD':
            result = amount / float(rates['USD'])
        elif to_currency == 'pl':
            result = amount / float(rates['pl'])
    # Виведення результату
        result_label.config(text=f"Результат: {result:.2f} {to_currency}")

    except ValueError:
         messagebox.showerror("Помилка", "Будь ласка, введіть коректну суму.")


# Створення головного вікна
root = tk.Tk()
root.title("Обмін валют")
root.geometry('500x500')
# Поле для введення суми
amount_label = tk.Label(root, text="Введіть суму:", font=('Arial',20))
amount_label.pack()

amount_entry = tk.Entry(root)
amount_entry.pack()

from_currency_var = tk.StringVar(value='UAH')
from_currency_menu = tk.OptionMenu(root, from_currency_var, 'UAH')
from_currency_menu.pack()

# Вибір валюти, на яку обмінюємо
to_currency_label = tk.Label(root, text="Виберіть валюту для отримання:", font=('Arial',20) )
to_currency_label.pack()

to_currency_var = tk.StringVar(value='EUR')
to_currency_menu = tk.OptionMenu(root, to_currency_var, 'USD', 'EUR', 'HAMSTR', 'pl')
to_currency_menu.pack()

# Кнопка для обміну
convert_button = tk.Button(root, text="Обміняти", command=convert_currency)
convert_button.pack()

# Мітка для результату
result_label = tk.Label(root, text="Результат: ", font=('Arial',24))
result_label.pack()

# Запуск головного циклу програми
root.mainloop()