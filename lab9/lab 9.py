import tkinter as tk
from tkinter import messagebox
import requests

def get_country_info():
    country_name = entry.get()
    if not country_name:
        messagebox.showwarning("Введіть назву країни", "Будь ласка, введіть назву країни.")
        return
    
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        country_data = response.json()[0]
        capital = country_data.get("capital", ["Немає даних"])[0]
        region = country_data.get("region", "Немає даних")
        population = country_data.get("population", "Немає даних")
        area = country_data.get("area", "Немає даних")
        currencies = ", ".join([currency["name"] for currency in country_data["currencies"].values()])
        
        result_text = (
            f"Назва країни: {country_name}\n"
            f"Столиця: {capital}\n"
            f"Регіон: {region}\n"
            f"Населення: {population}\n"
            f"Площа: {area} км²\n"
            f"Валюта: {currencies}"
        )
        
        result_label.config(text=result_text)
    else:
        messagebox.showerror("Помилка", "Не вдалося знайти інформацію про країну. Перевірте назву та спробуйте ще раз.")

root = tk.Tk()
root.title("Інформація про країну")

frame = tk.Frame(root)
frame.pack(pady=20, padx=20)

label = tk.Label(frame, text="Введіть назву країни:")
label.pack()

entry = tk.Entry(frame, width=30)
entry.pack(pady=5)

button = tk.Button(frame, text="Отримати інформацію", command=get_country_info)
button.pack(pady=10)

result_label = tk.Label(root, text="", justify="left", font=("Helvetica", 12))
result_label.pack(pady=10)

root.mainloop()
