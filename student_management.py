import sqlite3
from tkinter import *
from tkinter import ttk, messagebox

# ---------------- DATABASE --------------------
def connect_db():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            roll INTEGER PRIMARY KEY,
            name TEXT,
            course TEXT,
            fee INTEGER
        )
    """)
    conn.commit()
    conn.close()

connect_db()

# ---------------- FUNCTIONS --------------------
def add_student():
    if roll_var.get() == "" or name_var.get() == "":
        messagebox.showerror("Error", "All fields are required!")
        return
    
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?)", 
                       (roll_var.get(), name_var.get(), course_var.get(), fee_var.get()))
        conn.commit()
        messagebox.showinfo("Success", "Student added successfully!")
        fetch_students()
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Roll number already exists!")
    conn.close()

def fetch_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    student_table.delete(*student_table.get_children())
    for row in rows:
        student_table.insert("", END, values=row)
    conn.close()

def get_data(event):
    row = student_table.focus()
    data = student_table.item(row)["values"]
    if data:
        roll_var.set(data[0])
        name_var.set(data[1])
        course_var.set(data[2])
        fee_var.set(data[3])

def update_student():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE students SET name=?, course=?, fee=? WHERE roll=?
    """, (name_var.get(), course_var.get(), fee_var.get(), roll_var.get()))
    conn.commit()
    conn.close()
    messagebox.showinfo("Updated", "Student details updated successfully!")
    fetch_students()

def delete_student():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE roll=?", (roll_var.get(),))
    conn.commit()
    conn.close()
    messagebox.showinfo("Deleted", "Student deleted successfully!")
    fetch_students()

def clear_fields():
    roll_var.set("")
    name_var.set("")
    course_var.set("")
    fee_var.set("")

# ---------------- GUI --------------------
root = Tk()
root.title("Student Management System")
root.geometry("750x500")

title = Label(root, text="Student Management System", font=("Arial", 22, "bold"), fg="white", bg="blue")
title.pack(fill=X)

frame = Frame(root, pady=10)
frame.pack()

# Input fields
roll_var = StringVar()
name_var = StringVar()
course_var = StringVar()
fee_var = StringVar()

Label(frame, text="Roll No:").grid(row=0, column=0, padx=10, pady=5)
Entry(frame, textvariable=roll_var).grid(row=0, column=1)

Label(frame, text="Name:").grid(row=1, column=0, padx=10, pady=5)
Entry(frame, textvariable=name_var).grid(row=1, column=1)

Label(frame, text="Course:").grid(row=2, column=0, padx=10, pady=5)
Entry(frame, textvariable=course_var).grid(row=2, column=1)

Label(frame, text="Fees:").grid(row=3, column=0, padx=10, pady=5)
Entry(frame, textvariable=fee_var).grid(row=3, column=1)

# Buttons
btn_frame = Frame(root, pady=10)
btn_frame.pack()

Button(btn_frame, text="Add", width=10, command=add_student).grid(row=0, column=0, padx=10)
Button(btn_frame, text="Update", width=10, command=update_student).grid(row=0, column=1, padx=10)
Button(btn_frame, text="Delete", width=10, command=delete_student).grid(row=0, column=2, padx=10)
Button(btn_frame, text="Clear", width=10, command=clear_fields).grid(row=0, column=3, padx=10)

# Table (Treeview)
table_frame = Frame(root)
table_frame.pack()

scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
scroll_y = Scrollbar(table_frame, orient=VERTICAL)

student_table = ttk.Treeview(table_frame, columns=("roll","name","course","fee"),
                             xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=student_table.xview)
scroll_y.config(command=student_table.yview)

student_table.heading("roll", text="Roll No")
student_table.heading("name", text="Name")
student_table.heading("course", text="Course")
student_table.heading("fee", text="Fees")

student_table["show"] = "headings"

student_table.column("roll", width=80)
student_table.column("name", width=150)
student_table.column("course", width=120)
student_table.column("fee", width=80)

student_table.pack(fill=BOTH, expand=1)
student_table.bind("<ButtonRelease-1>", get_data)

fetch_students()

root.mainloop()


#cd C:\Users\Subramanya\Desktop

#python student_management.py

