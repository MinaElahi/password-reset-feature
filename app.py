import tkinter as tk  # import the Tkinter library

# Create the main app window
root = tk.Tk()

root.title("My Desktop App")
root.geometry("400x300")

# Add a heading label
heading_label = tk.Label(root, text="Reset Your Password", font=("Arial", 16))
heading_label.grid(row=0, column=0, columnspan=2, pady=10)

# Add a label and entry for the username
username_label = tk.Label(root, text="Username:")
username_label.grid(row=1, column=0, padx=20, pady=5, sticky="e")
username_entry = tk.Entry(root, width=30)
username_entry.grid(row=1, column=1, padx=20, pady=5)

# Add a label and entry for old password
old_password_label = tk.Label(root, text="Old Password:")
old_password_label.grid(row=2, column=0, padx=20, pady=5, sticky="e")
old_password_entry = tk.Entry(root, width=30, show="*")
old_password_entry.grid(row=2, column=1, padx=20, pady=5)

# Add a label and entry for new password
new_password_label = tk.Label(root, text="New Password:")
new_password_label.grid(row=3, column=0, padx=20, pady=5, sticky="e")
new_password_entry = tk.Entry(root, width=30, show="*")
new_password_entry.grid(row=3, column=1, padx=20, pady=5)

def reset_password():
    username = username_entry.get()
    old_password = old_password_entry.get()
    new_password= new_password_entry.get()

    if not username or not old_password or not new_password:
        tk.messagebox.showerror("Error", "All fields are required!")

    else: 
        tk.messagebox.showinfo("Success", "Password reset successfully!")  

reset_button = tk.Button(root, text="Reset Password")
reset_button.grid(row=4, column=1, pady=10)


# Run the application
root.mainloop()
