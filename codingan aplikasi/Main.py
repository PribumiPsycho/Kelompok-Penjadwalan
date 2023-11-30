import calendar
import tkinter as tk
from tkinter import ttk, messagebox

class ScheduleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Perjadwalan")
        self.root.geometry("1080x720")  # Set the window size to 1080 x 720

        # Set the background color to black
        self.root.configure(bg='#000000')

        # Variabel untuk menyimpan jadwal
        self.schedule_data = []

        # Create a style for consistent theming
        style = ttk.Style()
        style.theme_use("clam")  # Use the "clam" theme

        # Create a main frame with a pink border
        self.frame = tk.Frame(root, bg='#000000')
        self.frame.pack(fill='both', expand=True)

        # Create a sub-frame for the calendar on the left
        self.calendar_frame = ttk.Frame(self.frame, padding=(10, 10, 10, 10))
        self.calendar_frame.grid(row=0, column=0, sticky="nsew")

        # Create a sub-frame for the schedule on the right
        self.schedule_frame = ttk.Frame(self.frame, padding=(10, 10, 10, 10))
        self.schedule_frame.grid(row=0, column=1, sticky="nsew")

        # Set column weights for resizing
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(0, weight=1)

        # Create the calendar widgets
        self.create_calendar_widgets()

        # Create the schedule widgets
        self.create_schedule_widgets()

    def create_calendar_widgets(self):
        # Label and Entry for input year
        ttk.Label(self.calendar_frame, text="Tahun:", foreground='#FFFFFF').grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.year_var = tk.StringVar()
        year_entry = ttk.Entry(self.calendar_frame, textvariable=self.year_var)
        year_entry.grid(row=0, column=1, padx=5, pady=5)

        # Label and Entry for input month
        ttk.Label(self.calendar_frame, text="Bulan:", foreground='#FFFFFF').grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.month_var = tk.StringVar()
        month_entry = ttk.Entry(self.calendar_frame, textvariable=self.month_var)
        month_entry.grid(row=1, column=1, padx=5, pady=5)

        # Button to show the calendar
        show_button = ttk.Button(self.calendar_frame, text="Tampilkan Kalender", command=self.show_calendar)
        show_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Treeview to display the calendar
        self.tree = ttk.Treeview(self.calendar_frame, columns=[f"{i}" for i in range(7)], show="headings", height=10)
        for i, day in enumerate(["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]):
            self.tree.heading(f"{i}", text=day)
            self.tree.column(f"{i}", width=50, anchor="center")  # Adjust column width

        self.tree.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    def create_schedule_widgets(self):
        # Label and Entry for input event
        label_frame_event = tk.Frame(self.schedule_frame, bg='#000000')
        label_frame_event.pack(pady=5, anchor='e')

        self.label_event = tk.Label(label_frame_event, text="Acara:", bg='#000000', fg='#FFFFFF', font=('Arial', 14), bd=0, highlightthickness=0)
        self.label_event.pack()

        entry_frame_event = tk.Frame(self.schedule_frame, bg='#000000', highlightbackground='#FF34D2', highlightcolor='#FF34D2', highlightthickness=2)
        entry_frame_event.pack(pady=5, fill='x')

        self.entry_event = tk.Entry(entry_frame_event, bg='#000000', fg='#FFFFFF', insertbackground='#FF34D2', font=('Arial', 14))
        self.entry_event.pack(fill='x')

        # Label and Entry for input date
        self.label_date = tk.Label(self.schedule_frame, text="Waktu :", bg='#000000', fg='#FFFFFF', font=('Arial', 14))
        self.label_date.pack(pady=5, anchor='e')
        
        self.entry_date = tk.Entry(self.schedule_frame, bg='#000000', fg='#FFFFFF', highlightbackground='#FF34D2', highlightcolor='#FF34D2', highlightthickness=2, font=('Arial', 14))
        self.entry_date.pack(pady=5, fill='x')

        # Listbox to display the schedule
        self.listbox_schedule = tk.Listbox(self.schedule_frame, bg='#000000',fg='#FFFFFF', highlightbackground='#FF34D2', highlightcolor='#FF34D2', highlightthickness=2, font=('Arial', 14))
        self.listbox_schedule.pack(pady=5, fill='both', expand=True)

        # Buttons for main functions
        button_font = ('Arial', 14)

        self.btn_add = tk.Button(self.schedule_frame, text="Add", command=self.add_schedule, bg='#FF34D2', fg='#000000', font=button_font)
        self.btn_add.pack(side='right', padx=10, pady=5)

        self.btn_view = tk.Button(self.schedule_frame, text="View", command=self.view_schedule, bg='#FF34D2', fg='#000000', font=button_font)
        self.btn_view.pack(side='right', padx=10, pady=5)

        self.btn_edit = tk.Button(self.schedule_frame, text="Edit", command=self.edit_schedule, bg='#FF34D2', fg='#000000', font=button_font)
        self.btn_edit.pack(side='right', padx=10, pady=5)

        self.btn_delete = tk.Button(self.schedule_frame, text="Delete", command=self.delete_schedule, bg='#FF34D2', fg='#000000', font=button_font)
        self.btn_delete.pack(side='right', padx=10, pady=5)

    def add_schedule(self):
        event = self.entry_event.get()
        date = self.entry_date.get()

        if event and date:
            schedule_text = f"Acara saya: {event}, Tanggal: {date}"
            self.schedule_data.append(schedule_text)
            self.listbox_schedule.insert(tk.END, schedule_text)
            self.clear_entries()
        else:
            messagebox.showwarning("Peringatan", "Isi semua kolom!")

    def view_schedule(self):
        if not self.schedule_data:
            messagebox.showinfo("Info", "Tidak ada jadwal yang tersimpan.")
        else:
            schedule_text = "\n".join(self.schedule_data)
            messagebox.showinfo("Jadwal", schedule_text)

    def edit_schedule(self):
        selected_index = self.listbox_schedule.curselection()

        if selected_index:
            selected_index = selected_index[0]
            event, date = self.extract_data(self.schedule_data[selected_index])

            # Show window to edit schedule
            edit_window = tk.Toplevel(self.root)
            edit_window.title("Edit Jadwal")

            # Label and Entry for input event
            label_edit_event = tk.Label(edit_window, text="Acara:")
            label_edit_event.pack(pady=5)
            entry_edit_event = tk.Entry(edit_window)
            entry_edit_event.insert(0, event)
            entry_edit_event.pack(pady=5)

            # Label and Entry for input date
            label_edit_date = tk.Label(edit_window, text="Tanggal (dd/mm/yyyy):")
            label_edit_date.pack(pady=5)
            entry_edit_date = tk.Entry(edit_window)
            entry_edit_date.insert(0, date)
            entry_edit_date.pack(pady=5)

            # Button to save changes
            btn_save_changes = tk.Button(edit_window, text="Simpan Perubahan", command=lambda: self.save_changes(selected_index, entry_edit_event.get(), entry_edit_date.get(), edit_window))
            btn_save_changes.pack(pady=10)

        else:
            messagebox.showwarning("Peringatan", "Pilih jadwal yang ingin diubah.")

    def save_changes(self, index, new_event, new_date, edit_window):
        if new_event and new_date:
            new_schedule_text = f"Acara: {new_event}, Tanggal: {new_date}"
            self.schedule_data[index] = new_schedule_text
            self.listbox_schedule.delete(index)
            self.listbox_schedule.insert(index, new_schedule_text)
            edit_window.destroy()
            self.clear_entries()
        else:
            messagebox.showwarning("Peringatan", "Isi semua kolom!")

    def delete_schedule(self):
        selected_index = self.listbox_schedule.curselection()

        if selected_index:
            confirm = messagebox.askyesno("Konfirmasi", "Anda yakin ingin menghapus jadwal ini?")
            if confirm:
                selected_index = selected_index[0]
                self.listbox_schedule.delete(selected_index)
                del self.schedule_data[selected_index]
                self.clear_entries()
        else:
            messagebox.showwarning("Peringatan", "Pilih jadwal yang ingin dihapus.")

    def extract_data(self, schedule_text):
        parts = schedule_text.split(", ")
        event = parts[0].split(": ")[1]
        date = parts[1].split(": ")[1]
        return event, date

    def clear_entries(self):
        self.entry_event.delete(0, tk.END)
        self.entry_date.delete(0, tk.END)

    def show_calendar(self):
        year = int(self.year_var.get())
        month = int(self.month_var.get())
        cal_text = calendar.monthcalendar(year, month)

        # Delete all items from Treeview
        self.tree.delete(*self.tree.get_children())

        for week in cal_text:
            # Add a row for each week
            self.tree.insert('', 'end', values=week)

if __name__ == "__main__":
    root = tk.Tk()
    app = ScheduleApp(root)
    root.mainloop()
