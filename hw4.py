import tkinter as tk

def calculate_interest():
    try:
        p = float(principal_entry.get())
        r = float(rate_entry.get())
        t = float(time_entry.get())

        si = (p * r * t) / 100
        total = p + si

        result_label.config(text=f"Simple Interest: {si}\nTotal Amount: {total}")
    except:
        result_label.config(text="Invalid Input")

app = tk.Tk()
app.title("Interest Calculator")
app.geometry("300x250")

tk.Label(app, text="Principal").pack()
principal_entry = tk.Entry(app)
principal_entry.pack()

tk.Label(app, text="Rate (%)").pack()
rate_entry = tk.Entry(app)
rate_entry.pack()

tk.Label(app, text="Time (years)").pack()
time_entry = tk.Entry(app)
time_entry.pack()

tk.Button(app, text="Calculate", command=calculate_interest).pack(pady=10)

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()