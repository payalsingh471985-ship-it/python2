import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date

def calculate_age():
    try:
        day = int(day_var.get())
        month = int(month_var.get())
        year = int(year_var.get())
        

        birth_date = date(year, month, day)
        today = date.today()

    
        years = today.year - birth_date.year
        months = today.month - birth_date.month
        days = today.day - birth_date.day

        if days < 0:
            months -= 1
            days += 30  

        if months < 0:
            years -= 1
            months += 12

        result_label.config(
            text=f" You are {years} years, {months} months, {days} days old!",
            foreground="#00FFCC"
        )

    except Exception:
        messagebox.showerror("Error", "Please enter a valid date!")

root = tk.Tk()
root.title(" Age Calculator")
root.geometry("400x400")
root.configure(bg="#1e1e2f")

style = ttk.Style()
style.theme_use("clam")

style.configure("TLabel", background="#1e1e2f", foreground="white", font=("Segoe UI", 12))
style.configure("TButton", font=("Segoe UI", 11, "bold"), padding=6)
style.configure("TEntry", padding=5)

title_label = ttk.Label(root, text="Age Calculator", font=("Segoe UI", 18, "bold"))
title_label.pack(pady=20)

frame = ttk.Frame(root)
frame.pack(pady=10)

# Variables
day_var = tk.StringVar()
month_var = tk.StringVar()
year_var = tk.StringVar()

ttk.Label(frame, text="Day").grid(row=0, column=0, padx=5, pady=5)
ttk.Entry(frame, textvariable=day_var, width=8).grid(row=1, column=0, padx=5)

ttk.Label(frame, text="Month").grid(row=0, column=1, padx=5, pady=5)
ttk.Entry(frame, textvariable=month_var, width=8).grid(row=1, column=1, padx=5)

ttk.Label(frame, text="Year").grid(row=0, column=2, padx=5, pady=5)
ttk.Entry(frame, textvariable=year_var, width=10).grid(row=1, column=2, padx=5)

calc_btn = ttk.Button(root, text="Calculate Age", command=calculate_age)
calc_btn.pack(pady=20)

result_label = ttk.Label(root, text="", font=("Segoe UI", 12, "bold"))
result_label.pack(pady=20)

footer = ttk.Label(root, text="Made with Tkinter 💙", font=("Segoe UI", 9))
footer.pack(side="bottom", pady=10)

root.mainloop()