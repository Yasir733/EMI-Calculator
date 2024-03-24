import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np

def calculate_emi():
    principal = float(principal_entry.get())
    rate_of_interest = float(interest_entry.get()) / 12 / 100
    tenure = int(tenure_entry.get())
    
    emi = principal * rate_of_interest * ((1 + rate_of_interest) ** tenure) / (((1 + rate_of_interest) ** tenure) - 1)
    
    result_label.config(text=f'EMI: {emi:.2f} INR')

    # Calculate amortization schedule
    emi_values = []
    principal_remaining = principal
    for _ in range(tenure):
        interest_payment = principal_remaining * rate_of_interest
        principal_payment = emi - interest_payment
        principal_remaining -= principal_payment
        emi_values.append([principal_payment, interest_payment])
    
    # Plot amortization schedule
    plot_amortization_schedule(emi_values)

def plot_amortization_schedule(emi_values):
    principal_payments = [item[0] for item in emi_values]
    interest_payments = [item[1] for item in emi_values]
    
    plt.figure(figsize=(8, 6))
    plt.bar(np.arange(len(principal_payments)), principal_payments, label='Principal Payment')
    plt.bar(np.arange(len(interest_payments)), interest_payments, bottom=principal_payments, label='Interest Payment')
    
    plt.xlabel('Month')
    plt.ylabel('Payment Amount (INR)')
    plt.title('Amortization Schedule')
    plt.legend()
    plt.grid(True)
    
    plt.show()

# Create a tkinter window
root = tk.Tk()
root.title("EMI Calculator")

# Create labels and entry widgets
principal_label = ttk.Label(root, text="Principal Amount (INR):")
interest_label = ttk.Label(root, text="Rate of Interest (% per annum):")
tenure_label = ttk.Label(root, text="Tenure (months):")

principal_entry = ttk.Entry(root)
interest_entry = ttk.Entry(root)
tenure_entry = ttk.Entry(root)

calculate_button = ttk.Button(root, text="Calculate EMI", command=calculate_emi)
result_label = ttk.Label(root, text="")

# Arrange widgets using grid layout
principal_label.grid(row=0, column=0)
interest_label.grid(row=1, column=0)
tenure_label.grid(row=2, column=0)

principal_entry.grid(row=0, column=1)
interest_entry.grid(row=1, column=1)
tenure_entry.grid(row=2, column=1)

calculate_button.grid(row=3, column=0, columnspan=2)
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()



