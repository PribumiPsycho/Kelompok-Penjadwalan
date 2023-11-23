import tkinter as tk
from tkinter import ttk
import calendar

class SimpleCalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calendar")
        self.root.geometry("550x310")

        self.selected_year = tk.StringVar()
        self.selected_month = tk.StringVar()

        # Apply color theme
        self.root.configure(bg='#000000')

        self.create_widgets()

    def create_widgets(self):
        # Combobox for selecting the year
        label_year = tk.Label(self.root, text="Year:", bg='#000000', fg='#FF34D2')
        label_year.grid(row=0, column=0, padx=10, pady=10)

        self.combobox_year = ttk.Combobox(self.root, values=list(range(2020, 2031)), textvariable=self.selected_year, state='readonly')
        self.combobox_year.set(2020)
        self.combobox_year.grid(row=0, column=1, padx=10, pady=10)

        # Combobox for selecting the month
        label_month = tk.Label(self.root, text="Month:", bg='#000000', fg='#FF34D2')
        label_month.grid(row=0, column=2, padx=10, pady=10)

        self.combobox_month = ttk.Combobox(self.root, values=list(range(1, 13)), textvariable=self.selected_month, state='readonly')
        self.combobox_month.set(1)
        self.combobox_month.grid(row=0, column=3, padx=10, pady=10)

        # Button to display the calendar
        btn_show_calendar = tk.Button(self.root, text="Show Calendar", command=self.show_calendar, bg='#FF34D2', fg='#000000')
        btn_show_calendar.grid(row=0, column=4, padx=10, pady=10)

        # Frame as a container for the Text widget with a border
        frame_calendar = tk.Frame(self.root, bg='#000000', bd=5, relief='solid', highlightbackground='#FF34D2')
        frame_calendar.grid(row=1, column=0, columnspan=5, pady=10, padx=10)

        # Text widget to display the calendar
        self.calendar_text = tk.Text(frame_calendar, height=15, width=35, state=tk.DISABLED, bg='#000000', fg='#FFFFFF')
        self.calendar_text.pack()

    def show_calendar(self):
        year = int(self.selected_year.get())
        month = int(self.selected_month.get())

        cal_text = calendar.month(year, month)
        self.calendar_text.config(state=tk.NORMAL)
        self.calendar_text.delete(1.0, tk.END)
        self.calendar_text.insert(tk.END, cal_text)
        self.calendar_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleCalendarApp(root)
    root.mainloop()
