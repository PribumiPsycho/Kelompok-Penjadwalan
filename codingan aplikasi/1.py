import tkinter as tk
from tkinter import messagebox

class ScheduleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Perjadwalan")
        self.root.geometry("1080x720")  # Set the window size to 1920 x 1080

        # Set the background color to black
        self.root.configure(bg='#000000')

        # Variabel untuk menyimpan jadwal
        self.schedule_data = []

        # Create a label frame to hold all the elements with a pink border
        frame = tk.LabelFrame(root, text="Aplikasi Perjadwalan", bg='#000000', fg='#FFFFFF', bd=5, relief='solid', font=('Arial', 16))
        frame.pack(side='right', padx=10, pady=10, fill='y')  # Align to the right and fill vertically

        # Label dan Entry untuk input acara
        label_frame_event = tk.Frame(frame, bg='#000000')
        label_frame_event.pack(pady=5, anchor='e')

        self.label_event = tk.Label(label_frame_event, text="Acara:", bg='#000000', fg='#FFFFFF', font=('Arial', 14), bd=0, highlightthickness=0)
        self.label_event.pack()

        entry_frame_event = tk.Frame(frame, bg='#000000', highlightbackground='#FF34D2', highlightcolor='#FF34D2', highlightthickness=2)
        entry_frame_event.pack(pady=5, fill='x')

        self.entry_event = tk.Entry(entry_frame_event, bg='#000000', fg='#FFFFFF', insertbackground='#FF34D2', font=('Arial', 14))
        self.entry_event.pack(fill='x')

        # Label dan Entry untuk input tanggal
        self.label_date = tk.Label(frame, text="Waktu :", bg='#000000', fg='#FFFFFF', font=('Arial', 14))
        self.label_date.pack(pady=5, anchor='e')
        

        self.entry_date = tk.Entry(frame, bg='#000000', fg='#FFFFFF', highlightbackground='#FF34D2', highlightcolor='#FF34D2', highlightthickness=2, font=('Arial', 14))
        self.entry_date.pack(pady=5, fill='x')

        # Listbox untuk menampilkan jadwal
        self.listbox_schedule = tk.Listbox(frame, bg='#000000',fg='#FFFFFF', highlightbackground='#FF34D2', highlightcolor='#FF34D2', highlightthickness=2, font=('Arial', 14))
        self.listbox_schedule.pack(pady=5, fill='both', expand=True)

        # Tombol-tombol untuk fungsi utama
        button_font = ('Arial', 14)

        self.btn_add = tk.Button(frame, text="Add", command=self.add_schedule, bg='#FF34D2', fg='#000000', font=button_font)
        self.btn_add.pack(side='right', padx=10, pady=5)

        self.btn_view = tk.Button(frame, text="View", command=self.view_schedule, bg='#FF34D2', fg='#000000', font=button_font)
        self.btn_view.pack(side='right', padx=10, pady=5)

        self.btn_edit = tk.Button(frame, text="Edit", command=self.edit_schedule, bg='#FF34D2', fg='#000000', font=button_font)
        self.btn_edit.pack(side='right', padx=10, pady=5)

        self.btn_delete = tk.Button(frame, text="Delete", command=self.delete_schedule, bg='#FF34D2', fg='#000000', font=button_font)
        self.btn_delete.pack(side='right', padx=10, pady=5)


    def add_schedule(self):
        event = self.entry_event.get()
        date = self.entry_date.get()

        if event and date:
            schedule_text = f"Acara: {event}, Tanggal: {date}"
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

            # Tampilkan jendela untuk mengedit jadwal
            edit_window = tk.Toplevel(self.root)
            edit_window.title("Edit Jadwal")

            # Label dan Entry untuk input acara
            label_edit_event = tk.Label(edit_window, text="Acara:")
            label_edit_event.pack(pady=5)
            entry_edit_event = tk.Entry(edit_window)
            entry_edit_event.insert(0, event)
            entry_edit_event.pack(pady=5)

            # Label dan Entry untuk input tanggal
            label_edit_date = tk.Label(edit_window, text="Tanggal (dd/mm/yyyy):")
            label_edit_date.pack(pady=5)
            entry_edit_date = tk.Entry(edit_window)
            entry_edit_date.insert(0, date)
            entry_edit_date.pack(pady=5)

            # Tombol untuk menyimpan perubahan
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

    # Rest of your code remains the same...

if __name__ == "__main__":
    root = tk.Tk()
    app = ScheduleApp(root)
    root.mainloop()
