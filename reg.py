import tkinter as tk
from tkinter import messagebox
import openpyxl
from openpyxl import load_workbook

# Set up the main application window
root = tk.Tk()
root.title("Visitor Entry Form")
root.geometry("350x250")

file_path=r"E:\JANANI\python\registrations.xlsx"
A = openpyxl.load_workbook(file_path)
B = A["Data"]


# Function to handle data submission
def register_user():
    # Retrieve data from input fields
    name = entry_name.get()
    department = entry_department.get()
    meet = entry_meet.get()
    id = entry_id.get()
    phone = entry_phone.get()
    # Simple validation check
    if not name or not department or not id or not meet or not phone:
        messagebox.showerror("Error", "All fields are required!")
        
    else:
        # Display success message box
        messagebox.showinfo("Success", f"Registration Successful!\nWelcome, {name}!")
        B.append([name,department,meet,id,phone])
        A.save(file_path)
        clear_fields()

# Function to clear the form after submission
def clear_fields():
    entry_name.delete(0, tk.END)
    entry_department.delete(0, tk.END)
    entry_meet.delete(0, tk.END)
    entry_id.delete(0, tk.END)
    entry_phone.delete(0, tk.END)



# Heading Label
label_title = tk.Label(root, text="System Evaluation Lab - Visitor Entry Record", font=("Arial", 16, "bold"))
label_title.pack(pady=15)

# Container frame for the form fields
form_frame = tk.Frame(root)
form_frame.pack(pady=5)

# Name Layout
label_name = tk.Label(form_frame, text="Name:")
label_name.grid(row=0, column=0, sticky="w", pady=5)
entry_name = tk.Entry(form_frame, width=25)
entry_name.grid(row=0, column=1, pady=5)

# Department Layout
label_department = tk.Label(form_frame, text="Department / Company:")
label_department.grid(row=1, column=0, sticky="w", pady=5)
entry_department = tk.Entry(form_frame, width=25)
entry_department.grid(row=1, column=1, pady=5)

# ID Layout
label_id = tk.Label(form_frame, text="ID / Token Number:")
label_id.grid(row=2, column=0, sticky="w", pady=5)
entry_id = tk.Entry(form_frame, width=25)  # show="*" masks the password input
entry_id.grid(row=2, column=1, pady=5)

# Meet Layout
label_meet = tk.Label(form_frame, text="Whom to meet:")
label_meet.grid(row=3, column=0, sticky="w", pady=5)
entry_meet = tk.Entry(form_frame, width=25)  # show="*" masks the password input
entry_meet.grid(row=3, column=1, pady=5)

# Phone Layout
label_phone = tk.Label(form_frame, text="Phone Number:")
label_phone.grid(row=4, column=0, sticky="w", pady=5)
entry_phone = tk.Entry(form_frame, width=25)  # show="*" masks the password input
entry_phone.grid(row=4, column=1, pady=5)

# Submit Button
btn_submit = tk.Button(root, text="Register", command=register_user, bg="#4CAF50", fg="white", width=12)
btn_submit.pack(pady=15)

# Start the application loop
root.mainloop()
