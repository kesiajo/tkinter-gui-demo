import mongoengine
from models import EmployeeModel
from settings import MONGODB_HOST, MONGODB_DB_NAME
import tkinter as tk
from tkinter import ttk, font


def get_department_list():
    departments = EmployeeModel.objects.distinct("department")
    return departments


def search_department():
    # department = department_var.get()

    employees = EmployeeModel.objects(department=department_var.get())

    for item in result_tree.get_children():
        result_tree.delete(item)

    for employee in employees:
        result_tree.insert(
            '', 'end',
            values=(employee.emp_id, employee.emp_name, employee.department, employee.email)
        )


mongoengine.connect(host=MONGODB_HOST, db=MONGODB_DB_NAME)

# Create the main window
window = tk.Tk()
window.title("Employee Search")
window.geometry('1000x500')
window.configure(background="#FFFDD0")

style = ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground="orange", background="white", foreground="orange")
font_style = button_font = font.Font(family='Helvitica', size=14)

department_label = tk.Label(window, text="Select Department", background="#FFFDD0", foreground="black", font=font_style)
department_label.pack(padx=10, pady=10)
department_var = tk.StringVar()
department_combo = ttk.Combobox(window, textvariable=department_var, background="white", foreground="black")

for department in get_department_list():
    department_combo["values"] = (*department_combo["values"], department)
department_combo.pack()

search_button = tk.Button(window, text="Search", font=font_style, command=search_department, bg="orange",
                          fg="black", borderwidth=0)
search_button.pack(padx=15, pady=15)

columns = ("ID", "Name", "Department", "Email")
result_tree = ttk.Treeview(window, columns=columns, show="headings")

for col in columns:
    result_tree.heading(col, text=col)
    if col == 'Email':
        result_tree.column(col, width=200)
    else:
        result_tree.column(col, width=90)

result_tree.pack(fill=tk.X, padx=8, pady=8)

window.mainloop()
