import sqlite3
from tkinter import *
from tkinter import messagebox
#SQLite3 is a serverless and easy to use database software . 
#tkinter is used to create a user interface for the contactbook
# Database setup
def setup_db():
    con = sqlite3.connect('contacts.db')
    cobj = con.cursor()
    cobj.execute('''CREATE TABLE IF NOT EXISTS contacts
                 (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT, address TEXT)''')
    #a new field id is added for unique recognition of each contact
    con.commit()
    con.close()

# Add a new contact
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if name and phone and email and address:
        conn = sqlite3.connect('contacts.db')
        c = conn.cursor()
        c.execute("INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)",
                  (name, phone, email, address))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Contact added successfully!")
        clear_entries()
        view_contacts()
    else:
        messagebox.showwarning("Input Error", "Please fill all fields")

# View all contacts
def view_contacts():
    con = sqlite3.connect('contacts.db')
    cobj = con.cursor()
    cobj.execute("SELECT * FROM contacts")
    rows = cobj.fetchall()
    con.close()

    listbox_contacts.delete(0, END)
    for row in rows:
        listbox_contacts.insert(END, f"{row[1]} - {row[2]}")

# Search contacts
def search_contact():
    search_term = entry_search.get()
    con = sqlite3.connect('contacts.db')
    cobj = con.cursor()
    cobj.execute("SELECT * FROM contacts WHERE name LIKE ? OR phone LIKE ?", ('%'+search_term+'%', '%'+search_term+'%'))
    rows = cobj.fetchall()
    con.close()

    listbox_contacts.delete(0, END)
    for row in rows:
        listbox_contacts.insert(END, f"{row[1]} - {row[2]}")

# Update contact
def update_contact():
    selected = listbox_contacts.get(ACTIVE)
    if selected:
        con = sqlite3.connect('contacts.db')
        cobj = con.cursor()
        cobj.execute("UPDATE contacts SET name=?, phone=?, email=?, address=? WHERE id=?",
                  (entry_name.get(), entry_phone.get(), entry_email.get(), entry_address.get(), selected_contact_id))
        con.commit()
        con.close()
        messagebox.showinfo("Success", "Contact updated successfully!")
        clear_entries()
        view_contacts()
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to update")

# Delete contact
def delete_contact():
    selected = listbox_contacts.get(ACTIVE)
    if selected:
        con = sqlite3.connect('contacts.db')
        cobj = con.cursor()
        cobj.execute("DELETE FROM contacts WHERE id=?", (selected_contact_id,))
        con.commit()
        con.close()
        messagebox.showinfo("Success", "Contact deleted successfully!")
        clear_entries()
        view_contacts()
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to delete")

# Clear entry fields
def clear_entries():
    entry_name.delete(0, END)
    entry_phone.delete(0, END)
    entry_email.delete(0, END)
    entry_address.delete(0, END)

# Get selected contact details
def get_selected_contact(event):
    global selected_contact_id
    selected = listbox_contacts.get(ACTIVE)
    if selected:
        con = sqlite3.connect('contacts.db')
        cobj = con.cursor()
        cobj.execute("SELECT * FROM contacts WHERE name=? AND phone=?", tuple(selected.split(" - ")))
        row = cobj.fetchone()
        con.close()

        if row:
            selected_contact_id = row[0]
            entry_name.delete(0, END)
            entry_name.insert(END, row[1])
            entry_phone.delete(0, END)
            entry_phone.insert(END, row[2])
            entry_email.delete(0, END)
            entry_email.insert(END, row[3])
            entry_address.delete(0, END)
            entry_address.insert(END, row[4])

# GUI setup
root = Tk()
root.title("Contact Manager")

Label(root, text="Name").grid(row=0, column=0)
entry_name = Entry(root)
entry_name.grid(row=0, column=1)

Label(root, text="Phone").grid(row=1, column=0)
entry_phone = Entry(root)
entry_phone.grid(row=1, column=1)

Label(root, text="Email").grid(row=2, column=0)
entry_email = Entry(root)
entry_email.grid(row=2, column=1)

Label(root, text="Address").grid(row=3, column=0)
entry_address = Entry(root)
entry_address.grid(row=3, column=1)

Button(root, text="Add Contact", command=add_contact).grid(row=4, column=0)
Button(root, text="Update Contact", command=update_contact).grid(row=4, column=1)
Button(root, text="Delete Contact", command=delete_contact).grid(row=4, column=2)

Label(root, text="Search").grid(row=5, column=0)
entry_search = Entry(root)
entry_search.grid(row=5, column=1)
Button(root, text="Search", command=search_contact).grid(row=5, column=2)

listbox_contacts = Listbox(root, width=50)
listbox_contacts.grid(row=6, column=0, columnspan=3)
listbox_contacts.bind('<<ListboxSelect>>', get_selected_contact)

Button(root, text="View All Contacts", command=view_contacts).grid(row=7, column=0, columnspan=3)

setup_db()
view_contacts()

root.mainloop()