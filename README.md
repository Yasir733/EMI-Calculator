# EMI-Calculator
A small project on EMI calculation using Python modules


This Python script uses the tkinter library for creating a graphical user interface (GUI) to calculate the Equated Monthly Installment (EMI) for a loan based on user input for principal amount, rate of interest, and tenure. It also calculates and visualizes the amortization schedule.

Here's a brief explanation of the code:

1. **Import Libraries:**
   - `tkinter`: Used for creating the GUI.
   - `matplotlib.pyplot`: Used for plotting the amortization schedule.
   - `numpy`: Used for numerical computations.

2. **Define Functions:**
   - `calculate_emi()`: Takes user input for loan details, calculates the EMI, updates the result label, and calls `plot_amortization_schedule()` to plot the amortization schedule.
   - `plot_amortization_schedule()`: Plots the principal and interest payments for each month in a bar chart using matplotlib.

3. **Create GUI Elements:**
   - Labels (`ttk.Label`) for principal amount, rate of interest, and tenure.
   - Entry widgets (`ttk.Entry`) for user input.
   - Calculate button (`ttk.Button`) to trigger the calculation.
   - Result label (`ttk.Label`) to display the calculated EMI.

4. **Arrange Widgets:**
   - Uses the grid layout manager to arrange the GUI elements in rows and columns within the tkinter window.

5. **Main Functionality:**
   - Retrieves user input for loan details when the "Calculate EMI" button is clicked.
   - Calculates the EMI and updates the result label.
   - Calculates the amortization schedule and plots it using matplotlib.

6. **GUI Loop:**
   - Starts the tkinter event loop (`root.mainloop()`) to display and interact with the GUI.

Overall, this script provides a simple interface for users to calculate loan EMIs and visualize the corresponding amortization schedule.
