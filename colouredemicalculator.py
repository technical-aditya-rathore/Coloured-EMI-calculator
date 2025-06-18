

import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage


def calculate_emi():
    try:
        principal = float(entry_principal.get().strip())
        rate_of_interest = float(entry_rate.get().strip()) / 12 / 100
        tenure = int(entry_tenure.get().strip()) * 12

        emi = principal * rate_of_interest * \
            ((1 + rate_of_interest) ** tenure) / \
            (((1 + rate_of_interest) ** tenure) - 1)
        emi = round(emi, 2)

        label_result.config(text=f"EMI: ₹ {emi}")
    except ValueError:
        messagebox.showerror(
            "Input Error", "Please enter valid numeric values.")


root = tk.Tk()
root.title("EMI Calculator")
root.geometry("400x400")

try:
    background_image = PhotoImage(
        file=r"c:/Users/ADMIN/Downloads/pexels-umaraffan499-21787.jpg")
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)
    background_label.lower()
except Exception as e:
    print(f"Background image failed to load: {e}")

frame = tk.Frame(root, bg='lightblue', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.6, anchor='n')

label_principal = tk.Label(frame, text="Loan Amount (₹):",
                           bg='lightblue', fg='darkblue', font=('Helvetica', 12))
label_principal.pack(pady=5)
entry_principal = tk.Entry(frame, font=('Helvetica', 12))
entry_principal.pack(pady=5)

label_rate = tk.Label(frame, text="Annual Interest Rate (%):",
                      bg='lightblue', fg='darkblue', font=('Helvetica', 12))
label_rate.pack(pady=5)
entry_rate = tk.Entry(frame, font=('Helvetica', 12))
entry_rate.pack(pady=5)

label_tenure = tk.Label(frame, text="Tenure (Years):",
                        bg='lightblue', fg='darkblue', font=('Helvetica', 12))
label_tenure.pack(pady=5)
entry_tenure = tk.Entry(frame, font=('Helvetica', 12))
entry_tenure.pack(pady=5)

button_calculate = tk.Button(frame, text="Calculate EMI", command=calculate_emi,
                             bg='darkblue', fg='white', font=('Helvetica', 12))
button_calculate.pack(pady=10)

label_result = tk.Label(root, text="EMI: ₹ 0.00", font=(
    "Helvetica", 16), bg='lightgreen', fg='black')
label_result.pack(pady=20)

root.mainloop()
